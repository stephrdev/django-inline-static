import distutils.dir_util
from unittest import mock

import pytest
from django.utils.safestring import SafeText

from inline_static.loader import load_staticfile
from inline_static.templatetags import inline_static_tags


class TestInlineStaticfileTag:

    def setup(self):
        load_staticfile._cache.clear()

    def test_invalid_path(self, settings):
        settings.DEBUG = True
        with pytest.raises(ValueError) as exc:
            inline_static_tags.inline_staticfile('foo.txt')
        assert 'not found' in str(exc.value)

    def test_invalid_path_fail_silently(self, settings):
        settings.DEBUG = False
        assert inline_static_tags.inline_staticfile('foo.txt') == ''

    def test_cache(self, settings):
        settings.DEBUG = False

        # collectstatic for the poor. Faster than calling the management command.
        distutils.dir_util.copy_tree(settings.STATICFILES_DIRS[0], settings.STATIC_ROOT)

        assert inline_static_tags.inline_staticfile('test.txt').strip() == 'Lorem Ipsum'

        with mock.patch(
            'django.contrib.staticfiles.storage.staticfiles_storage.path'
        ) as path_mock:
            assert inline_static_tags.inline_staticfile(
                'test.txt').strip() == 'Lorem Ipsum'

        assert path_mock.called is False

    def test_valid_path(self, settings):
        settings.DEBUG = True
        assert inline_static_tags.inline_staticfile(
            'test.txt').strip() == 'Lorem Ipsum'

    def test_not_safe(self, settings):
        settings.DEBUG = True
        assert isinstance(inline_static_tags.inline_staticfile(
            'test.txt'), SafeText) is False


class TestInlineJavascriptTag:

    @pytest.fixture(autouse=True)
    def setup(self, settings):
        settings.DEBUG = True

    def test_content(self):
        assert inline_static_tags.inline_javascript(
            'js/module.js').strip() == 'var foo = {bar: 23}'

    def test_is_safe(self):
        assert isinstance(inline_static_tags.inline_javascript(
            'js/module.js'), SafeText) is True


class TestInlineStyleTag:

    @pytest.fixture(autouse=True)
    def setup(self, settings):
        settings.DEBUG = True

    def test_content(self):
        assert inline_static_tags.inline_style('css/all.css').strip().splitlines() == [
            'body { background-image: url("/static/img/noimage.jpg"); }',
            '.extimg { background-image: url("https://placekitten.com/g/200/300"); }'
        ]

    def test_content_absolute_static_url(self, settings):
        settings.STATIC_URL = 'https://cdn.local/'
        assert inline_static_tags.inline_style('css/all.css').strip().splitlines() == [
            'body { background-image: url("https://cdn.local/img/noimage.jpg"); }',
            '.extimg { background-image: url("https://placekitten.com/g/200/300"); }'
        ]

    def test_content_absolute_static_url_path(self, settings):
        settings.STATIC_URL = 'https://cdn.local/static/'
        assert inline_static_tags.inline_style('css/all.css').strip().splitlines() == [
            'body { background-image: url("https://cdn.local/static/img/noimage.jpg"); }',
            '.extimg { background-image: url("https://placekitten.com/g/200/300"); }'
        ]

    def test_is_safe(self):
        assert isinstance(inline_static_tags.inline_style(
            'css/all.css'), SafeText) is True

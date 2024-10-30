from ckan.plugins import SingletonPlugin, implements, IConfigurer, IRoutes, toolkit
from flask import abort

class RestrictAccessPlugin(SingletonPlugin):
    implements(IConfigurer)
    implements(IRoutes, inherit=True)

    def update_config(self, config):
        # Add custom CSS and template override path to hide the logout icon
        toolkit.add_public_directory(config, 'ckanext/restrictaccess/public')
        toolkit.add_template_directory(config, 'ckanext/restrictaccess/templates')

    def before_map(self, map):
    # Define routes to be blocked
        restricted_paths = [
            '/user/login',
            '/user/_logout',
            '/user/logged_out',
            '/user/logged_out_redirect',
            '/user/reset',
            '/user/register'
        ]

        for path in restricted_paths:
            map.connect(f'restricted_{path}', path, controller='ckanext.restrictaccess.plugin:block_access')

        return map

    def block_access():
        toolkit.response.status = 403
        return toolkit.render('403.html', extra_vars={'message': 'Access to this page is restricted.'})


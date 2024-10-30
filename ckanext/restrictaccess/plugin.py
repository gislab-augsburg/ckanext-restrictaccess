from ckan.plugins import SingletonPlugin, implements, IConfigurer, IRoutes, toolkit

class RestrictAccessPlugin(SingletonPlugin):
    implements(IConfigurer)
    implements(IRoutes, inherit=True)

    def update_config(self, config):
        # Add custom CSS and template override path to hide the logout icon
        config['extra_public_paths'] = ','.join([
            config.get('extra_public_paths', ''),
            'ckanext/restrictaccess/public',
        ])
        config['extra_template_paths'] = ','.join([
            config.get('extra_template_paths', ''),
            'ckanext/restrictaccess/templates',
        ])

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
            map.connect(f'restricted_{path}', path, controller='ckanext.restrictaccess.plugin:RestrictAccessController', action='block_access')

        return map


class RestrictAccessController(toolkit.BaseController):
    def block_access(self):
        toolkit.abort(403, 'Access to this page is restricted.')

from plone.app.layout.viewlets.common import LogoViewlet


class LogoViewlet(LogoViewlet):
    def update(self):
        super(LogoViewlet, self).update()
        self.logo_tag = '<img src="' + self.navigation_root_url + '/++theme++mazu.theme/logo.jpg" alt="MaZu Site Logo">'


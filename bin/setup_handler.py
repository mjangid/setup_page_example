import os, sys, logging
import splunk.admin as admin
import splunk.entity as en
import splunk.Intersplunk

logfile = os.sep.join([os.environ['SPLUNK_HOME'], 'var', 'log', 'splunk', 'setup_example.log'])
logging.basicConfig(filename=logfile, level=logging.DEBUG)

class ConfigApp(admin.MConfigHandler):
    def setup(self):
        logging.debug('[SETUP_PAGE] begin=setup')
        if self.requestedAction == admin.ACTION_EDIT:
            for arg in ['username', 'password', 'host', 'port', 'appname', 'my_bool_variable']:
                self.supportedArgs.addOptArg(arg)
        logging.debug('[SETUP_PAGE] end=setup')

    def handleList(self, confInfo):
        logging.debug('[SETUP_PAGE] begin=handleList')
        confDict = self.readConf("anyfile")
        if None != confDict:
            for stanza, settings in confDict.items():
                for key, val in settings.items():
                    if key in ['my_bool_variable']:
                        if int(val) == 1:
                            val = '1'
                        else:
                            val = '0'
                    if key in ['username'] and val in [None, '']:
                        val = ''
                    if key in ['password'] and val in [None, '']:
                        val = ''
                    if key in ['host'] and val in [None, '']:
                        val = ''
                    if key in ['port'] and val in [None, '']:
                        val = ''
                    if key in ['appname'] and val in [None, '']:
                        val = ''
                    confInfo[stanza].append(key, val)
        logging.debug('[SETUP_PAGE] end=handleList')

    def handleEdit(self, confInfo):
        logging.debug('[SETUP_PAGE] begin=handleEdit')
        if self.callerArgs.data['password'][0] in [None, '']:
            self.callerArgs.data['password'][0] = ''

        if self.callerArgs.data['username'][0] in [None, '']:
            self.callerArgs.data['username'][0] = ''

        if self.callerArgs.data['host'][0] in [None, '']:
            self.callerArgs.data['host'][0] = ''

        if self.callerArgs.data['port'][0] in [None, '']:
            self.callerArgs.data['port'][0] = ''

        if self.callerArgs.data['appname'][0] in [None, '']:
            self.callerArgs.data['appname'][0] = ''

        if int(self.callerArgs.data['my_bool_variable'][0]) == 1:
            self.callerArgs.data['my_bool_variable'][0] = '1'
        else:
            self.callerArgs.data['my_bool_variable'][0] = '0'

        self.writeConf('anyfile', 'onetime_setup', self.callerArgs.data)
        logging.debug('[SETUP_PAGE] end=handleEdit')

# initialize the handler
logging.debug('[SETUP_PAGE] initialize the handler')
admin.init(ConfigApp, admin.CONTEXT_NONE)

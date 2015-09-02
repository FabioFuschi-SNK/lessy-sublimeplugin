import sublime, sublime_plugin
import subprocess
import platform
import os
#
# view.run_command('lessy')
class LessyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
		sels = self.view.sel()
		for sel in sels:
			bla = self.view.substr(sel)  

			lessc_command = "lessc"
			#
			if platform.system() == 'Windows':
				# change command from lessc to lessc.cmd on Windows,
				# only lessc.cmd works but lessc doesn't
				lessc_command = 'lessc.cmd'
			else:
				# if is not Windows, modify the PATH
				env = os.getenv('PATH')
				env = env + ':/usr/bin:/usr/local/bin:/usr/local/sbin'
				os.environ['PATH'] = env
				# check for the existance of the less compiler, exit if it can't be located
				if subprocess.call(['which', lessc_command]) == 1:
					return sublime.error_message('lessy error: `lessc` is not available')


			p =subprocess.Popen(["echo '"+bla+"' | "+lessc_command+" -"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
			output, stderr = p.communicate()

			if (stderr):
				return sublime.error_message('lessy error: ' + str(stderr))
			else:
				self.view.replace(edit, sel, output)
			
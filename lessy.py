import sublime, sublime_plugin
import subprocess
#
# view.run_command('lessy')
class LessyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
		sels = self.view.sel()
		for sel in sels:
			bla = self.view.substr(sel)  
			p =subprocess.Popen(["echo '"+bla+"' | /usr/local/bin/lessc -"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
			output, stderr = p.communicate()

			if (stderr):
				return sublime.error_message('lessy error: ' + str(stderr))
			else:
				self.view.replace(edit, sel, output)
			
from fman import DirectoryPaneListener, show_alert, YES, NO, \
	ApplicationCommand, show_status_message, load_json, save_json
from fman.fs import exists, mkdir
from fman.url import dirname, join, basename

_SETTINGS_FILE = 'Synchronized Browsing.json'

class ToggleSynchronizedBrowsing(ApplicationCommand):
	def __call__(self):
		settings = load_json(_SETTINGS_FILE, default={})
		enabled_new = not settings.get('enabled', True)
		settings['enabled'] = enabled_new
		save_json(_SETTINGS_FILE)
		status = 'ON' if enabled_new else 'OFF'
		show_status_message(
			'Synchronized browsing is %s.' % status, timeout_secs=3
		)

class SynchBrowsing(DirectoryPaneListener):
	def on_command(self, command_name, args):
		is_enabled = load_json(_SETTINGS_FILE, default={}).get('enabled', True)
		if not is_enabled:
			return
		other_pane = self._other_pane
		if command_name == 'go_up':
			try:
				other_pane.set_path(dirname(other_pane.get_path()))
			except FileNotFoundError:
				# This for instance happens when going up from file:///
				# (to  file://) on UNIX.
				pass
		elif command_name == 'open_directory':
			dir_name = basename(args['url'])
			dest_other = join(other_pane.get_path(), dir_name)
			if exists(dest_other):
				other_pane.set_path(dest_other)
			else:
				choice = show_alert(
					'%s does not exist. Do you want to create it?' % dir_name,
					YES | NO, YES
				)
				if choice == YES:
					mkdir(dest_other)
					other_pane.set_path(dest_other)
	@property
	def _other_pane(self):
		panes = self.pane.window.get_panes()
		return panes[(panes.index(self.pane) + 1) % len(panes)]
import sublime_plugin
import sublime
import re


class ConcatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        region = sublime.Region(0, view.size())

        path = '/'.join(self.view.file_name().split('/')[0:-1])
        full_name = self.view.file_name().split('/')[-1]
        extension = full_name.split('.')[-1]
        file_name = '.'.join(full_name.split('.')[0:-1])

        test = '/{0,2}@import url\(\'(.+)\'\);'
        i = self.view.find(test, 0)
        if i:
            new_view = window.new_file()
            new_view.set_name(file_name + '.cat.' + extension)
            region = sublime.Region(0, view.size())
            content = view.substr(region)

            try:
                syntax_file = self.view.settings().get('syntax')
                new_view.set_syntax_file(syntax_file)
            except KeyError:
                print 'no syntax'
                pass

            edit = new_view.begin_edit('cat')
            new_view.insert(edit, 0, content)

            while new_view.find(test, 0):
                i = new_view.find(test, 0)
                content = new_view.substr(i)
                m = re.search(test, content)

                if m:
                    included = m.group(1)

                    try:
                        f = open(path + '/' + included)
                        file_content = f.read()
                        new_view.replace(edit, i, file_content)
                        f.close()
                    except IOError:
                        print 'cannot open', included
                        raise

            new_view.end_edit(edit)
            window.run_command("save")
            window.run_command("build")

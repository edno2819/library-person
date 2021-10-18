import pywinauto


class Desktop():
    def __init__(self, backend='win32'):
        pywinauto.timings.Timings.window_find_timeout = 60
        pywinauto.timings.Timings.app_start_timeout = 60
        pywinauto.timings.Timings.app_connect_timeout = 60
        self.app = pywinauto.application.Application(backend=backend)
        self.backend = backend

    def set_params(self, search_params):
        return  search_params if type(search_params) == dict else {'best_match':search_params}

    def find_app(self, search_params, timeout=60):
        try:
            self.win = self.app.connect(**search_params, timeout=timeout)
            return self.win
        except:
            False

    def start_app(self, search_params:dict):
        self.app.start(search_params['path'])

    def find_window(self, search_params, wait=5):
        try:
            search_params=self.set_params(search_params)
            self.win.window(**search_params).wait('exists', wait)
            self.dlg = self.win.window(**search_params)
            self.dlg.set_focus()
            return self.dlg
        except:
            return False

    def find_element(self, search_params:dict, wait=5):
        try:
            search_params=self.set_params(search_params)
            self.dlg.child_window(**search_params).wait('exists', wait)
            self.elem = self.dlg.child_window(**search_params)
                
            self.elem.set_focus()
            return self.elem
        except: 
            return False

    def get_element_attribute(self,search_params,attribute):
        return self.find_element(search_params).element_info.__getattribute__(attribute)

    def get_window_attribute(self,attribute):
        return self.dlg.element_info.__getattribute__(attribute)

    def get_window_top(self):
        self.dlg = self.win.top_window()
        self.dlg.set_focus()
        return True

    def switch_dlg(self, method):
        if method == 'save':
            self.saved_dlg = self.dlg
        elif method == 'restore':
            self.dlg = self.saved_dlg
        else:
            raise Exception('Pick an available method.')

    def click(self, search_params:dict):
        self.find_element(search_params).click()

    def click_input(self, search_params:dict):
        ''' Use elementos que n forem do tipo Button'''
        self.find_element(search_params).click_input()

    def fill(self, search_params:dict, text:str):
        self.find_element(search_params).set_text('').set_text(text)

    def check(self, search_params:dict, state:bool):
        elem = self.find_element(search_params)

        if elem.backend.name == 'win32':
            while elem.is_checked() != state:
                elem.click()
 
        else:
            while elem.get_toggle_state() != int(state):
                elem.click()  

    def select(self, search_params:dict, select:str):
        self.find_element(search_params).select(select)

    def press_keys_from_element(self, search_params:dict, keys:str):
        self.find_element(search_params).type_keys(keys)

    def press_keys(self, keys:str):
        pywinauto.keyboard.send_keys(keys)

    def press_keys_from_window(self,keys:str):
        self.dlg.type_keys(keys)
    
    def close_window(self):
        self.dlg.close()

    def close_module(self):
        self.win.kill()

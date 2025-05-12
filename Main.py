from ui.app import App

# import repo.mongo_repo as mongo_repo
app_window = None


def get_app_window():
   global app_window
   if app_window is None:
      app_window = App()
      app_window.mainloop()
   return app_window

def main():
   # mongo_repo.initialize()
   window = get_app_window()
   window.mainloop()


if __name__ == "__main__":
   get_app_window()

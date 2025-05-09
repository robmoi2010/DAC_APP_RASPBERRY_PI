from app import App
import mongo_repo

if __name__ == "__main__":
    mongo_repo.initialize()
    dacApp = App()
    dacApp.mainloop()

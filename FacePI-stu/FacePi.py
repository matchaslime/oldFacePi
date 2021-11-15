import fire, json

class FacePi:
    def readConfig(self):
        with open('Config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config

    def test(self):

        print(self.readConfig())
        config = self.readConfig()
        print(config['title'])

if __name__ == '__main__':
    fire.Fire(FacePi)
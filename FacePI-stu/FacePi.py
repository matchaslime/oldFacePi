import fire, json

class FacePi:
    def readConfig(self):
        with open('Config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config

    def writeConfig(self, config):
        with open('Config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f)


    def setConfig(self):
        config = self.readConfig()
        print('每個參數後[]為預設值，按 ENTER 即表示不更動')
        api_key = input(f'請輸入有效的 API_KEY[{config["api_key"]}]')
        if api_key: config['api_key'] = api_key
        title = input(f'請輸入title[{config["title"]}]')
        if title: config['title'] = title

        self.writeConfig(config)

if __name__ == '__main__':
    fire.Fire(FacePi)
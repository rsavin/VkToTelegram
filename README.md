# VkToTelegram

The pipe between VK public communities and Telegram messenger. It checks VK communities walls every minute and sends
 new posts to the Telegram users.


## Usage

You have to create `properties.json` file with the following params:

```json
{
  "walls": [
    "<wall_id1>",
    "<wall_id2>",
    "<wall_id3>"
  ],
  "telegram_bot_token": "<your_telegram_bot_token>",
  "user_ids": [
    "<telegram_user_id1>",
    "<telegram_user_id2>",
    "<telegram_user_id3>"
  ]
}
```

The `walls` parameter is the list of communities (or users) walls. It's the same parameter as `domain` in the  [wall.get](https://vk.com/dev/wall.get) request.

The `telegram_bot_token` parameter is the token of your telegram bot which will send messages.

The `user_ids` parameters is the ids of telegram users which will receive messages.

Run:
```
python vk_to_telegram.py properties.json
```

## License

    Copyright 2015 Roman Savin

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.






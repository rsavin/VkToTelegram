# VkToTelegram

The pipe between VK public communities and Telegram messenger. It checks VK communities walls every minute and sends
 new posts to the Telegram users.


## Usage

You have to create `properties.json` with the following params:

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






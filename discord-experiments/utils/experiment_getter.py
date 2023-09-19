from typing import Any, Dict, Optional
import aiohttp
import json

import typing


async def get_experiments(*, session: Optional[aiohttp.ClientSession] = None) -> Optional[Dict[str, Any]]:
    """
    Gets or fetches all experiments
    """

    s: aiohttp.ClientSession = session or aiohttp.ClientSession()

    async with s as s_:
        async with s_.get("https://raw.githubusercontent.com/discordexperimenthub/assyst-tags/main/experiment-rollout/data.json") as response:
            if response.status == 200:
                raw_content: str = await response.text()

                try:
                    json_data: typing.Union[typing.Dict[typing.Any, typing.Any], typing.Any] = json.loads(
                        raw_content)
                    return json_data

                except json.JSONDecodeError as e:
                    print(
                        "Failed to convert 'raw_content' (of type '{}') into a JSON".format(
                            raw_content.__class__.__name__)
                    )
                    print(
                        e.with_traceback()
                    )
                    return None
            else:
                print(
                    "Response status wasn't the expected, expected '200' and got '{}'".format(
                        response.status)
                )

                return None
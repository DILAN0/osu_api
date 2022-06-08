import requests

API_URL = 'https://osu.ppy.sh/api/v2'


class osu:
    def get_token(*client_s):
        data = {
            'client_id': '10055',
            'client_secret': client_s,
            'grant_type': 'client_credentials',
            'scope': 'public'
        }

        response = requests.post('https://osu.ppy.sh/oauth/token', data=data)

        return response.json().get('access_token')

    def pp(self, id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self}'
        }

        params = {
            'mode': 'osu',
            'limit': 5
        }
        # https://osu.ppy.sh/docs/index.html #gamemode
        # ..........
        response = requests.get(f'{API_URL}/users/{id}', params=params, headers=headers)

        beatmapset_data = response.json()

        pp = beatmapset_data['statistics']['pp']

        return pp

    def avatar(self, id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self}'
        }

        params = {
            'mode': 'osu',
            'limit': 5
        }
        # https://osu.ppy.sh/docs/index.html #gamemode
        # ..........
        response = requests.get(f'{API_URL}/users/{id}', params=params, headers=headers)

        beatmapset_data = response.json()

        avatar = beatmapset_data['avatar_url']

        return avatar

class score:
    def get_user_scores(self, id, type, offset):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self}'
        }

        params = (
            ('include_fails', '0'),
            ('mode', 'osu'),
            ('limit', '1'),
            ('offset', f'{offset}'),
        )

        res = requests.get(f'https://osu.ppy.sh/api/v2/users/{id}/scores/{type}', headers=headers, params=params)

        score_assets = res.json()

        return score_assets



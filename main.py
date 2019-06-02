import requests
import bs4


def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def send_login(firstName, lastName):
	print response.text

if __name__ == '__main__':
	res = requests.session()
	#res.get("https://login.crowdcompass.com/login/names")
	r = res.get("https://svc.crowdcompass.com/login/e/E2HnUZ3rp1/login?authorized_redirect=https%3A%2F%2Fevent.crowdcompass.com%2F2019techintern%2Factivity%2FanzXndMzGS&confirm_base_url=https%3A%2F%2Fsvc.crowdcompass.com%2FE2HnUZ3rp1%2Fconfirm%2F&device=")
	headers = {
	    'pragma': 'no-cache',
	    'origin': 'https://login.crowdcompass.com',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
	    'content-type': 'application/json',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'cache-control': 'no-cache',
	    'authority': 'svc.crowdcompass.com',
	    'referer': 'https://login.crowdcompass.com/login/names',
	}

	data = '{"login_attempt":{"event_oid":"E2HnUZ3rp1","workflow":"verification_code","authorized_redirect":"https://event.crowdcompass.com/2019techintern/activity/anzXndMzGS","device":"","confirm_base_url":"https://svc.crowdcompass.com/E2HnUZ3rp1/confirm/","answers":[{"challenge_id":"names","first_name":"Christopher","last_name":"Lambert"}]}}'

	response = requests.put('https://svc.crowdcompass.com/login/e/E2HnUZ3rp1/login/challenges/names', headers=headers, data=data)


	data = '{"login_attempt":{"event_oid":"E2HnUZ3rp1","workflow":"verification_code","authorized_redirect":"https://event.crowdcompass.com/2019techintern/activity/anzXndMzGS","device":"","confirm_base_url":"https://svc.crowdcompass.com/E2HnUZ3rp1/confirm/","answers":[{"challenge_id":"names","ok":true,"first_name":"Christopher","last_name":"Lambert"},{"challenge_id":"verification_code","verification_code":"' + raw_input("Code: ") + '"}]}}'

	response = res.put('https://svc.crowdcompass.com/login/e/E2HnUZ3rp1/login/challenges/verification_code', headers=headers, data=data)
	print response.text.partition("code=")[2].partition("%")[0]
	print res.cookies.get_dict()
	raw_input("CONTINUE? ")
	r = res.get('https://event.crowdcompass.com/auth/callback/event_site?auth_action=log_in&auth_method=crowdcompass_reg&code=593eef78f23e71972ff57912eea8%3Ar&event=E2HnUZ3rp1&response_type=code&redirect_uri=%2F2019techintern%2Factivity%2FanzXndMzGS', allow_redirects=True)
	for val in r.history:
		print val
	print r.text
	raw_input("CONTINUE 2? ")
	r = res.get(response.json()['login_attempt']['authorized_redirect'],  allow_redirects=True)
	print r.text
	r = res.get("https://accounts.crowdcompass.com/client/v3/user/events/E2HnUZ3rp1/schedule_items/by_date/2019-06-02?_release=2019050100",  allow_redirects=True)
	print r.text
	#print r.text
	#res = grabSite(url)
	#page = bs4.BeautifulSoup(res.text, 'lxml')



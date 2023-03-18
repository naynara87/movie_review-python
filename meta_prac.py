

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#meta tag 불러옴
ogtitle = soup.select_one('meta[property="og:title"]')['content']
ogdesc = soup.select_one('meta[property="og:description"]')['content']
ogimage = soup.select_one('meta[property="og:image"]')['content']
print(ogtitle,ogdesc,ogimage)
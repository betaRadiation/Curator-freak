import requests 
from bs4 import BeautifulSoup 

def main():
    r = requests.get('https://store.steampowered.com/curator/42948398-cultcraft-%2528on-dingus%2529/#browse')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='browse_content') 
    content = s.find_all('div', class_='recommendation') 

    print(content)

if __name__ == "__main__":
    main()

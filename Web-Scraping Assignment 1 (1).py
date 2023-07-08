#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


#write a python program to display all the header tags from wikipedia.org and make data frame


# In[3]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)


# In[6]:


soup


# In[7]:


header=[]
for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)


# In[8]:


header


# In[ ]:


#write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data frame


# In[9]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[10]:


page


# In[11]:


soup=BeautifulSoup(page.content)


# In[12]:


soup


# In[13]:


paper_titles=[]


# In[14]:


for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    paper_titles.append(i.text)


# In[15]:


paper_titles


# In[16]:


authors_list=[]


# In[17]:


for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authors_list.append(i.text)
authors_list


# In[18]:


published_dates=[]


# In[19]:


for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    published_dates.append(i.text)
published_dates


# In[20]:


paper_urls=[]


# In[21]:


for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    paper_urls.append(i.get('href'))
paper_urls


# In[22]:


import pandas as pd
data = {
    "Paper Title": paper_titles,
    "Authors": authors_list,
    "Published Date": published_dates,
    "Paper URL": paper_urls
}
df = pd.DataFrame(data)


# In[23]:


df


# In[ ]:


#Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make a dataframe


# In[24]:


page=requests.get('https://www.cnbc.com/world/?region=world')


# In[25]:


page


# In[26]:


soup=BeautifulSoup(page.content)


# In[27]:


soup


# In[28]:


headlines=[]


# In[29]:


for i in soup.find_all('a',class_="LatestNews-headline"):
    headlines.append(i.text)


# In[30]:


headlines


# In[31]:


times=[]


# In[32]:


for i in soup.find_all('span',class_="LatestNews-wrapper"):
    times.append(i.text)
times


# In[33]:


news_links=[]


# In[34]:


for i in soup.find_all('a',class_='LatestNews-headline'):
    news_links.append(i.get('href'))


# In[35]:


news_links


# In[36]:


df=pd.DataFrame({'Headlines':headlines,'Times':times,'News_links':news_links})


# In[37]:


df


# In[ ]:


#President of India


# In[39]:


page= requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[40]:


page


# In[41]:


soup=BeautifulSoup(page.content)


# In[42]:


soup


# In[43]:


names=[]


# In[44]:


for i in soup.find_all('div',class_="presidentListing"):
    names.append(i.text)


# In[45]:


names


# In[46]:


df=pd.DataFrame({'Names':names})


# In[47]:


df


# In[ ]:


#top10 odi team (men)


# In[58]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[59]:


page


# In[60]:


soup=BeautifulSoup(page.content)


# In[61]:


soup


# In[62]:


odi=[]


# In[63]:


for i in soup.find_all('span',class_="u-hide-phablet"):
    odi.append(i.text)


# In[64]:


odi


# In[65]:


team_list=['Australia', 'Pakistan', 'India', 'New Zealand', 'England', 'South Africa', 'Bangladesh', 'Sri Lanka', 'Afghanistan', 'West Indies', 'Zimbabwe', 'Scotland', 'Ireland', 'Nepal', 'Netherlands', 'United States', 'Namibia', 'Oman', 'UAE', 'Papua New Guinea']
top_10 = team_list[:10]
top_10


# In[88]:


rating_1=[]


# In[91]:


for i in soup.find_all('td',class_="rankings-block__banner--rating u-text-right"):
    rating_1.append(i.text)


# In[92]:


rating_1


# In[95]:


rating_1=['118']


# In[81]:


rating_2=[]


# In[82]:


for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating_2.append(i.text)


# In[83]:


rating_2


# In[97]:


rating_2=['116',
 '115',
 '104',
 '101',
 '101',
 '98',
 '85',
 '82',
 '69',
 '57',
 '48',
 '40',
 '35',
 '34',
 '29',
 '29',
 '25',
 '14',
 '4']


# In[98]:


rating_list=rating_1+rating_2


# In[99]:


rating_list


# In[100]:


rating_10=rating_list[:10]


# In[101]:


rating_10


# In[105]:


matches_points1=[]


# In[106]:


for i in soup.find_all('td',class_="rankings-block__banner--matches"):
    matches_points1.append(i.text)


# In[107]:


matches_points1


# In[122]:


macthes_points1=['23']


# In[123]:


matches_points1


# In[119]:


matches_points2=['2714']


# In[120]:


matches_points2


# In[116]:


matches_points3=[]


# In[117]:


for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches_points3.append(i.text)


# In[118]:


matches_points3


# In[125]:



data = matches_points1+matches_points2+['20', '2,316', '33', '3,807', '27', '2,806', '24', '2,426', '19', '1,910', '25', '2,451', '28', '2,378', '13', '1,067', '32', '2,201', '27', '1,530', '30', '1,451', '22', '887', '38', '1,340', '24', '816', '29', '855', '28', '813', '21', '522', '39', '554', '28', '106']

matches = data[::2]
points = data[1::2]

print(matches)
print(points)


# In[126]:


matches_10=matches[:10]


# In[127]:


matches_10


# In[128]:


points_10=points[:10]


# In[129]:


points_10


# In[ ]:





# In[130]:


df=pd.DataFrame({'Top_10':top_10,'Rating_10':rating_10,'Matches_10':matches_10,'Points_10':points_10})


# In[131]:


df


# In[ ]:


#top 10 odi batsman(men)


# In[148]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')


# In[149]:


page


# In[150]:


soup=BeautifulSoup(page.content)


# In[151]:


soup


# In[161]:


name1=['Babar Azam']


# In[162]:


name1


# In[139]:


names2=[]


# In[140]:


for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    names2.append(i.text)


# In[141]:


names2


# In[164]:


names = name1+['\nRassie van der Dussen\n', '\nFakhar Zaman\n', '\nImam-ul-Haq\n', '\nShubman Gill\n', '\nHarry Tector\n', '\nDavid Warner\n', '\nVirat Kohli\n', '\nQuinton de Kock\n', '\nRohit Sharma\n', '\nSteve Smith\n', '\nShai Hope\n', '\nJason Roy\n', '\nJonny Bairstow\n', '\nJos Buttler\n', '\nMushfiqur Rahim\n', '\nKane Williamson\n', '\nDavid Miller\n', '\nAlex Carey\n', '\nTom Latham\n', '\nJoe Root\n', '\nPaul Stirling\n', '\nShreyas Iyer\n', '\nNicholas Pooran\n', '\nTamim Iqbal\n', '\nRahmat Shah\n', '\nIbrahim Zadran\n', '\nTravis Head\n', '\nSikandar Raza\n', '\nGerhard Erasmus\n', '\nHeinrich Klaasen\n', '\nGlenn Maxwell\n', '\nTemba Bavuma\n', '\nShakib Al Hasan\n', '\nScott Edwards\n', '\nShikhar Dhawan\n', '\nKariyawasa Asalanka\n', '\nPathum Nissanka\n', '\nDawid Malan\n', '\nLokesh Rahul\n', '\nLitton Das\n', '\nSean Williams\n', '\nAiden Markram\n', '\nMartin Guptill\n', '\nMahmudullah\n', '\nNajibullah Zadran\n', '\nGeorge Munsey\n', '\nAssad Vala\n', '\nDevon Conway\n', '\nAndrew Balbirnie\n', '\nHashmatullah Shaidi\n', '\nVriitya Aravind\n', '\nMitchell Marsh\n', '\nDaryl Mitchell\n', '\nHaris Sohail\n', '\nKusal Mendis\n', '\nAqib Ilyas\n', '\nIshan Kishan\n', '\nKyle Coetzer\n', '\nMohammad Rizwan\n', "\nMax O'Dowd\n", '\nMuhammad Waseem\n', '\nAaron Jones\n', '\nGajanand Singh\n', '\nZeeshan Maqsood\n', '\nMichael Leask\n', '\nJanneman Malan\n', '\nRichard Berrington\n', '\nMarnus Labuschagne\n', '\nMohammad Nabi\n', '\nDhananjaya de Silva\n', '\nMonank Patel\n', '\nR.K. Paudel\n', '\nWill Young\n', '\nHardik Pandya\n', '\nHenry Nicholls\n', '\nAasif Sheikh\n', '\nAyaan Khan\n', '\nSteven Taylor\n', '\nJatinder Singh\n', '\nCraig Ervine\n', '\nRahmanullah Gurbaz\n', '\nMarcus Stoinis\n', '\nKashyap Prajapati\n', '\nMichael van Lingen\n', '\nMitchell Santner\n', '\nGeorge Dockrell\n', '\nDasun Shanaka\n', '\nAvishka Fernando\n', '\nPhilip Salt\n', '\nBrandon King\n', '\nCurtis Campher\n', '\nAgha Salman\n', '\nDimuth Karunaratne\n', '\nVikramjit Singh\n', '\nMatthew Cross\n', '\nAsif Khan\n', '\nRyan Burl\n', '\nShamarh Brooks\n', '\nFinn Allen\n']
top_10=names[:10]


# In[165]:


top_10


# In[172]:


country1=['Pakistan']


# In[173]:


country1


# In[166]:


country2=[]


# In[167]:


for i in soup.find_all('span',class_="table-body__logo-text"):
    country2.append(i.text)


# In[168]:


country2


# In[174]:


country =country1+['SA', 'PAK', 'PAK', 'IND', 'IRE', 'AUS', 'IND', 'SA', 'IND', 'AUS', 'WI', 'ENG', 'ENG', 'ENG', 'BAN', 'NZ', 'SA', 'AUS', 'NZ', 'ENG', 'IRE', 'IND', 'WI', 'BAN', 'AFG', 'AFG', 'AUS', 'ZIM', 'NAM', 'SA', 'AUS', 'SA', 'BAN', 'NED', 'IND', 'SL', 'SL', 'ENG', 'IND', 'BAN', 'ZIM', 'SA', 'NZ', 'BAN', 'AFG', 'SCO', 'PNG', 'NZ', 'IRE', 'AFG', 'UAE', 'AUS', 'NZ', 'PAK', 'SL', 'OMA', 'IND', 'SCO', 'PAK', 'NED', 'UAE', 'USA', 'USA', 'OMA', 'SCO', 'SA', 'SCO', 'AUS', 'AFG', 'SL', 'USA', 'NEP', 'NZ', 'IND', 'NZ', 'NEP', 'OMA', 'USA', 'OMA', 'ZIM', 'AFG', 'AUS', 'OMA', 'NAM', 'NZ', 'IRE', 'SL', 'SL', 'ENG', 'WI', 'IRE', 'PAK', 'SL', 'NED', 'SCO', 'UAE', 'ZIM', 'WI', 'NZ']
country_10=country[:10]
country_10


# In[190]:


rating1=['886']


# In[191]:


rating1


# In[184]:


rating2=[]


# In[188]:


for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating2.append(i.text)


# In[189]:


rating2


# In[192]:


rating = rating1+['777', '755', '745', '738', '726', '726', '719', '718', '707', '702', '684', '682', '669', '658', '653', '652', '643', '631', '631', '631', '625', '624', '624', '621', '620', '617', '616', '615', '614', '612', '612', '609', '603', '585', '580', '573', '572', '572', '571', '570', '566', '557', '556', '551', '539', '537', '536', '528', '526', '525', '524', '523', '522', '515', '515', '513', '511', '511', '510', '508', '505', '501', '494', '492', '491', '490', '490', '490', '488', '487', '486', '480', '480', '479', '479', '475', '473', '467', '464', '464', '463', '461', '459', '457', '455', '454', '451', '448', '447', '447', '444', '444', '442', '441', '440', '439', '437', '437', '434']
rating_10=rating[:10]
rating_10


# In[193]:


df=pd.DataFrame({'Top_10':top_10,'Country_10':country_10,'Rating_10':rating_10})


# In[194]:


df


# In[ ]:


#top 10 odi bowlers(men)


# In[199]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[200]:


page


# In[201]:


soup=BeautifulSoup(page.content)


# In[202]:


soup


# In[206]:


name1=[]


# In[207]:


for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    name1.append(i.text)


# In[208]:


name1


# In[209]:


name1=['Josh Hazlewood']


# In[210]:


name1


# In[203]:


names2=[]


# In[204]:


for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    names2.append(i.text)


# In[205]:


names2


# In[211]:


names = name1+['\nMohammed Siraj\n', '\nMitchell Starc\n', '\nMatt Henry\n', '\nTrent Boult\n', '\nAdam Zampa\n', '\nRashid Khan\n', '\nShaheen Afridi\n', '\nMujeeb Ur Rahman\n', '\nMohammad Nabi\n', '\nMark Watt\n', '\nChris Woakes\n', '\nShakib Al Hasan\n', '\nKagiso Rabada\n', '\nPat Cummins\n', '\nJofra Archer\n', '\nAkeal Hosein\n', '\nAlzarri Joseph\n', '\nBernard Scholtz\n', '\nMustafizur Rahman\n', '\nSaurabh Netravalkar\n', '\nKuldeep Yadav\n', '\nMehedi Hasan\n', '\nSandeep Lamichhane\n', '\nLungi Ngidi\n', '\nAndy McBrine\n', '\nJasprit Bumrah\n', '\nMark Adair\n', '\nWanindu Hasaranga\n', '\nAdil Rashid\n', '\nMohammad Shami\n', '\nMaheesh Theekshana\n', '\nMohammad Nawaz\n', '\nMark Wood\n', '\nKeshav Maharaj\n', '\nRichard Ngarava\n', '\nMitchell Santner\n', '\nDavid Willey\n', '\nChristopher Sole\n', '\nRuben Trumpelmann\n', '\nBilal Khan\n', '\nHaris Rauf\n', '\nShardul Thakur\n', '\nYuzvendra Chahal\n', '\nTabraiz Shamsi\n', '\nJoshua Little\n', '\nTaskin Ahmed\n', '\nShadab Khan\n', '\nAayan Afzal Khan\n', '\nZeeshan Maqsood\n', '\nTim Southee\n', '\nSafyaan Sharif\n', '\nDushmantha Chameera\n', '\nBlessing Muzarabani\n', '\nKaleemullah\n', '\nFred Klaassen\n', '\nTaijul Islam\n', '\nRohan Mustafa\n', '\nNosthush Kenjige\n', '\nAnrich Nortje\n', '\nLachlan Ferguson\n', '\nDipendra Airee\n', '\nSikandar Raza\n', '\nAssad Vala\n', '\nChad Soper\n', '\nLogan van Beek\n', '\nSam Curran\n', '\nZahoor Khan\n', '\nJason Holder\n', '\nSean Abbott\n', '\nMoeen Ali\n', '\nMohammad Wasim\n', '\nJunaid Siddique\n', '\nAshton Agar\n', '\nDhananjaya de Silva\n', '\nCraig Young\n', '\nHardik Pandya\n', '\nSompal Kami\n', '\nRavindra Jadeja\n', '\nSimi Singh\n', '\nNaseem Shah\n', '\nIsh Sodhi\n', '\nAryan Dutt\n', '\nMichael Leask\n', '\nTangeni Lungameni\n', '\nJhye Richardson\n', '\nKaran KC\n', '\nReece Topley\n', '\nHasan Ali\n', '\nWayne Parnell\n', '\nFazalhaq Farooqi\n', '\nAndile Phehlukwayo\n', '\nBrandon McMullen\n', '\nNisarg Patel\n', '\nKasun Rajitha\n', '\nHenry Shipley\n', '\nM. Prasidh Krishna\n', '\nHamza Tahir\n', '\nLalit Rajbanshi\n', '\nEbadot Hossain\n']
names_10=names[:10]
names_10


# In[222]:


team1=['Aus']


# In[223]:


team1


# In[218]:


teams=[]


# In[219]:


for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)


# In[220]:


teams


# In[224]:


teams = team1+['IND', 'AUS', 'NZ', 'NZ', 'AUS', 'AFG', 'PAK', 'AFG', 'AFG', 'SCO', 'ENG', 'BAN', 'SA', 'AUS', 'ENG', 'WI', 'WI', 'NAM', 'BAN', 'USA', 'IND', 'BAN', 'NEP', 'SA', 'IRE', 'IND', 'IRE', 'SL', 'ENG', 'IND', 'SL', 'PAK', 'ENG', 'SA', 'ZIM', 'NZ', 'ENG', 'SCO', 'NAM', 'OMA', 'PAK', 'IND', 'IND', 'SA', 'IRE', 'BAN', 'PAK', 'UAE', 'OMA', 'NZ', 'SCO', 'SL', 'ZIM', 'OMA', 'NED', 'BAN', 'UAE', 'USA', 'SA', 'NZ', 'NEP', 'ZIM', 'PNG', 'PNG', 'NED', 'ENG', 'UAE', 'WI', 'AUS', 'ENG', 'PAK', 'UAE', 'AUS', 'SL', 'IRE', 'IND', 'NEP', 'IND', 'IRE', 'PAK', 'NZ', 'NED', 'SCO', 'NAM', 'AUS', 'NEP', 'ENG', 'PAK', 'SA', 'AFG', 'SA', 'SCO', 'USA', 'SL', 'NZ', 'IND', 'SCO', 'NEP', 'BAN']
teams_10=teams[:10]
teams_10


# In[228]:


ratings1=[]


# In[229]:


for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    ratings1.append(i.text)


# In[230]:


ratings1


# In[225]:


ratings2=[]


# In[226]:


for i in soup.find_all('td',class_="table-body__cell rating"):
    ratings2.append(i.text)


# In[227]:


ratings2


# In[231]:


ratings = ratings1+['691', '686', '667', '660', '652', '640', '630', '630', '626', '621', '612', '610', '600', '597', '596', '594', '592', '589', '587', '583', '576', '576', '568', '562', '562', '552', '549', '547', '547', '540', '534', '524', '523', '521', '518', '515', '514', '511', '508', '507', '505', '505', '503', '500', '499', '499', '498', '494', '488', '487', '486', '482', '482', '478', '477', '477', '476', '475', '475', '475', '470', '468', '464', '462', '456', '454', '451', '451', '448', '441', '440', '440', '438', '435', '430', '428', '427', '427', '424', '424', '424', '423', '423', '421', '421', '421', '418', '415', '410', '409', '408', '406', '403', '403', '400', '395', '388', '388', '385']
ratings_10=ratings[:10]
ratings_10


# In[232]:


df=pd.DataFrame({'Names_10':names_10,'Teams_10':teams_10,'Ratings_10':ratings_10})


# In[233]:


df


# In[ ]:


#Top 10 odi team (women)


# In[234]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[235]:


page


# In[236]:


soup=BeautifulSoup(page.content)


# In[237]:


soup


# In[238]:


teams=[]


# In[239]:


for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)


# In[240]:


teams


# In[241]:


teams=['Australia',
 'England',
 'South Africa',
 'India',
 'New Zealand',
 'West Indies',
 'Bangladesh',
 'Sri Lanka',
 'Thailand',
 'Pakistan',
 'Ireland',
 'Netherlands',
 'Zimbabwe']
teams_10=teams[:10]
teams_10


# In[248]:


matches1=['21']


# In[249]:


matches1


# In[250]:


matches2=[]


# In[251]:


for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches2.append(i.text)


# In[252]:


matches2


# In[265]:


data = ['28', '3,342', '26', '3,098', '27', '2,820', '28', '2,688', '29', '2,743', '14', '977', '12', '820', '12', '806', '27', '1,678', '16', '605', '10', '90', '11', '0']

list1 = data[::2] 
list2 = data[1::2]  

print(list1)
print(list2)



# In[267]:


matches=matches1+list1


# In[269]:


matches_10=matches[:10]


# In[270]:


matches_10


# In[271]:


points=[]


# In[272]:


for i in soup.find_all('td',class_="rankings-block__banner--points"):
    points.append(i.text)


# In[273]:


points


# In[276]:


points_all=points+list2


# In[277]:


points_all


# In[279]:


points_10=points_all[:10]
points_10


# In[280]:


rating1=[]


# In[281]:


for i in soup.find('td',class_="rankings-block__banner--rating u-text-right"):
    rating1.append(i.text)


# In[282]:


rating1


# In[284]:


rating1=['172']
rating1


# In[285]:


ratings2=[]


# In[286]:


for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings2.append(i.text)


# In[287]:


ratings2


# In[292]:


ratings_all=rating1+ratings2
ratings_all


# In[294]:


ratings_10=ratings_all[:10]
ratings_10


# In[295]:


df=pd.DataFrame({'Teams_10':teams_10,'Matches_10':matches_10,'Points_10':points_10,'Ratings_10':ratings_10})


# In[296]:


df


# In[ ]:


# Top 10 odi batsmen (women)


# In[297]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')


# In[298]:


page


# In[300]:


soup=BeautifulSoup(page.content)


# In[301]:


soup


# In[302]:


name=[]


# In[305]:


for i in soup.find('div',class_="rankings-block__banner--name"):
    name.append(i.text)


# In[306]:


name


# In[307]:


name1=[]


# In[308]:


for i in soup.find_all('td',class_="table-body__cell name"):
    name1.append(i.text)


# In[309]:


name1


# In[311]:


names=name+name1
names


# In[313]:


names_10=names[:10]
names_10


# In[314]:


team=[]


# In[315]:


for i in soup.find('div',class_="rankings-block__banner--nationality"):
    team.append(i.text)


# In[316]:


team


# In[318]:


team=['SL']
team


# In[322]:


team1=[]


# In[323]:


for i in soup.find_all('span',class_="table-body__logo-text"):
    team1.append(i.text)


# In[324]:


team1


# In[326]:


team_all=team+team1
team_all


# In[327]:


team_10=team_all[:10]


# In[328]:


team_10


# In[329]:


rating=[]


# In[335]:


for i in soup.find('div',class_="rankings-block__banner--rating"):
    rating.append(i.text)


# In[336]:


rating


# In[341]:


rating=['758']
rating


# In[334]:


rating1=[]


# In[337]:


for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating1.append(i.text)


# In[342]:


rating1


# In[343]:


rating_all=rating+rating1
rating_all


# In[344]:


rating_10=rating_all[:10]


# In[345]:


rating_10


# In[346]:


df=pd.DataFrame({'Names_10':names_10,'Teams_10':team_10,'Rating_10':rating_10})


# In[347]:


df


# In[ ]:


# Top 10 odi all-rounder(women)


# In[420]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')


# In[421]:


page


# In[422]:


soup=BeautifulSoup(page.content)


# In[423]:


soup


# In[429]:


name1=[]


# In[430]:


for i in soup.find('div',class_="rankings-block__banner--name-large"):
    name1.append(i.text)


# In[431]:


name1


# In[432]:


name2=[]


# In[433]:


for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    name2.append(i.text)


# In[434]:


name2


# In[435]:


name_all=name1+name2
name_all


# In[436]:


name_10=name_all[:10]
name_10


# In[438]:


country1=[]


# In[441]:


for i in soup.find('div',class_="rankings-block__banner--nationality"):
    country1.append(i.text)


# In[442]:


country1


# In[451]:


country1=['WI']
country1


# In[445]:


country2=[]


# In[446]:


for i in soup.find_all('span',class_="table-body__logo-text"):
    country2.append(i.text)


# In[447]:


country2


# In[453]:


country_all=country1+country2


# In[454]:


country_all


# In[455]:


country_10=country_all[:10]


# In[456]:


country_10


# In[457]:


rating=[]


# In[458]:


for i in soup.find('div',class_="rankings-block__banner--rating"):
    rating.append(i.text)


# In[459]:


rating


# In[460]:


rating1=[]


# In[461]:


for i in soup.find_all('td',class_="table-body__cell rating"):
    rating1.append(i.text)


# In[462]:


rating1


# In[463]:


rating_all=rating+rating1


# In[464]:


rating_10=rating_all[:10]


# In[465]:


rating_10


# In[468]:


df=pd.DataFrame({'Names_10':name_10,'Teams_10':country_10,'Ratings_10':rating_10})


# In[469]:


df


# In[ ]:


#write a python program to scrape mentioned details from dineout.co.in and make data frame


# In[480]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")


# In[481]:


page


# In[482]:


soup= BeautifulSoup(page.content)
soup


# In[483]:


titles = []


# In[484]:


for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)


# In[485]:


titles


# In[496]:


cuisine=[]


# In[497]:


for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])


# In[498]:


cuisine


# In[499]:


loc=[]


# In[501]:


for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    loc.append(i.text)


# In[502]:


loc


# In[503]:


ratings=[]


# In[504]:


for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)


# In[505]:


ratings


# In[506]:


img_url=[]


# In[507]:


for i in soup.find_all('img',class_="no-img"):
    img_url.append(i.get('data-src'))


# In[508]:


img_url


# In[509]:


df=pd.DataFrame({'Titles':titles,'Cuisine':cuisine,'Location':loc,'Ratings':ratings,'Img_Url':img_url})


# In[510]:


df


# In[ ]:





# In[ ]:





# In[ ]:





import requests
import csv


# get csv file
GetWebSite = requests.get('https://static.data.gouv.fr/resources/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/20220124-190654/sp-pos-quot-fra-2022-01-24-19h06.csv')
url_content = GetWebSite.content
csv_file = open('downloaded.csv', 'wb')
csv_file.write(url_content)
csv_file.close()


# read csv file
file = open('downloaded.csv')
print(file)

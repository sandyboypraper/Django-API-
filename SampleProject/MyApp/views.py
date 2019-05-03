from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

 

@api_view(["POST"])
def Homes(Homesdata):
    
	options = Options()
    options.headless = True


    driver = webdriver.Firefox(options = options)
    driver.get("https://www.nestaway.com/search_new/?locality="+place+"&per_page=30&min_price=&max_price=&isgrid=&city="+city)

    house_boxes = driver.find_elements_by_xpath('//div[@class = "cardContent"]')

    total = len(house_boxes)

    listi = []
	
	for i in range(total):



        h_title = ''
        h_location = ''
        h_rent = ''
        r_avail = '0'


        try:
    	    h_title = house_boxes[i].find_elements_by_class_name("houseTittle")[0].text
        except:
    	    h_title = 'NIL'


        try:
    	    h_location = house_boxes[i].find_elements_by_class_name("houseSeoTittle")[0].get_attribute("title").split(',')[1]
        except:
    	    h_location = 'NIL'


        try:
    	    r_avail = house_boxes[i].find_elements_by_class_name("houseOtherInfo")[0].find_elements_by_tag_name("span")[2].text.split()[1]
        except:
    	    r_avail = '0'


        try:
    	    h_rent = house_boxes[i].find_elements_by_class_name("houseRentInfo")[0].find_elements_by_class_name("houseRent")[0].text.split()[3]
        except:
    	    h_rent = 'NIL'

        result = "('Property Name': '" + h_title + "' , Location: '"+h_location + "' , Available_rooms: '"+ r_avail + "' , rent: '" + h_rent + "' , )"

    	listi.add(result)

    return JsonResponse(listi)




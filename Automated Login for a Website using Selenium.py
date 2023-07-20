#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time # Introduce Delay between the operations


# In[2]:


# Create a connection with your browser

browser = webdriver.Chrome()

# Maximize the Browser window
browser.maximize_window()

# Open the Website
browser.get("https://www.hackveda.in/one2one")
time.sleep(2)


# In[3]:


username = browser.find_element("id", "email")
username


# In[4]:


username.send_keys("jamalepravin2001@gmail.com")
time.sleep(2)


# In[5]:


password = browser.find_element("id", "password")
password.send_keys("63")
time.sleep(2)


# In[6]:


button = browser.find_element("id", "login_btn")
time.sleep(5)
button.click()



#<button id="login_btn" type="button" class="button rounded green wide ae-9 cropBottom done" name="button">Sign in</button>


# In[ ]:





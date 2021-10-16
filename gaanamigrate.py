import driver_setup

import time

driver = driver_setup.get_driver()
handles = driver.window_handles
driver.switch_to.window(handles[1])
print(driver.title)
# current_url = "https://gaana.com/playlist/gaanauser89309842-nwyxh-16oct-qk52mj0l3w"
# driver.get(current_url)
driver.implicitly_wait(10)
song_names = driver.find_elements_by_xpath('//a/span[@class="t_over"]')
album_names = driver.find_elements_by_xpath('//div/a[@class="t_over"]')
l1 = [song.text for song in song_names]
l2 = [album.text for album in album_names]
not_found = []

driver.switch_to.window(handles[0])

print(driver.title)
search_box = driver.find_element_by_xpath('//input[@role="searchbox"]')
for i in range(72):
    search_box.clear()
    print(l1[i] + " " + l2[i])
    search_box.send_keys(l1[i] + " " + l2[i])
    time.sleep(2)
    if driver.find_elements_by_xpath('//button/span[@aria-label="Add to Playlist"]'):
        driver.find_element_by_xpath('(//button/span[@aria-label="Add to Playlist"])[1]').click()
    else:
        not_found.append(l1[i] + " " + l2[i])

print(not_found)

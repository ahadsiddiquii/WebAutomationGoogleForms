from selenium import webdriver
import time
import random

def render_form(form_url,web):
    web.get(form_url)

def radio_selection(web, radio_button_choice, default):
    choices = int(0)
    n = int(0)
    choices = len(radio_button_choice)
    n = random.randint(0, choices-1)
    try:
        radio_button_selected = web.find_element_by_xpath(radio_button_choice[n])
        radio_button_selected.click()
    except IndexError:
        print("index is incorrect")
        radio_button_selected = web.find_element_by_xpath(default)
        radio_button_selected.click()

def time_spent_online(web):
    radio_button_choice = [
        [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div'
        ],
        [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div'
        ],
        [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div'
        ],
        [
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div',
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div',
        ],
    ]
    for item in radio_button_choice:
        choices = int(0)
        choices = len(item)

        n = random.randint(0, choices-1)
        try:
            radio_button_selected = web.find_element_by_xpath(item[n])
            radio_button_selected.click()
            time.sleep(1)
        except IndexError:
            radio_button_selected = web.find_element_by_xpath(item[n])
            radio_button_selected.click()
            print("index is incorrect")




def submit_next_button(web, path):
    button_selected = web.find_element_by_xpath(path)
    button_selected.click()


if __name__ == '__main__':
    web = webdriver.Chrome()
    render_form('https://docs.google.com/forms/d/1YYRFl95uKFsB0vnAKiIrAnH5UODk8EJM_W0VJvYDZGI/viewform?edit_requested=true',web)
    for i in range(0,40):
        # waiting 2 seconds for the form to render properly
        time.sleep(2)
        # age selection
        print("age selection")
        age_selection_choice = ['//*[@id="i5"]/div[3]/div',
                               '//*[@id="i8"]/div[3]/div',
                               '//*[@id="i11"]/div[3]/div',
                               '//*[@id="i14"]/div[3]/div'
                               ]
        radio_selection(web, age_selection_choice,'//*[@id="i5"]/div[3]/div')
        # next button
        submit_next_button(web, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        # waiting 2 seconds for the form to render properly
        time.sleep(2)
        # social_interests_choice
        print("social interests")
        social_interests_choice = ['//*[@id="i6"]/div[2]',
                               '//*[@id="i9"]/div[2]',
                               '//*[@id="i12"]/div[2]',
                               '//*[@id="i15"]/div[2]',
                               '//*[@id="i18"]/div[2]',
                               '//*[@id="i21"]/div[2]',
                               '//*[@id="i24"]/div[2]'
                               ]
        radio_selection(web, social_interests_choice, '//*[@id="i6"]/div[2]')
        # time.sleep(1)
        # updates_via_internet_choice
        print("updates via internet")
        updates_via_internet_choice = ['//*[@id="i34"]/div[3]/div',
                               '//*[@id="i37"]/div[3]/div',
                               '//*[@id="i40"]/div[3]/div'
                               ]
        radio_selection(web, updates_via_internet_choice, '//*[@id="i34"]/div[3]/div')
        # time.sleep(1)
        # wake_up_at_night_choice
        print("wake up at night")
        wake_up_at_night_choice = ['//*[@id="i47"]/div[3]/div',
                               '//*[@id="i50"]/div[3]/div'
                               ]
        radio_selection(web, wake_up_at_night_choice, '//*[@id="i47"]/div[3]/div')
        # time.sleep(1)
        # stay_up_late_for_videogames_choice
        print("stay up late for videogames")
        stay_up_late_for_videogames_choice = ['//*[@id="i57"]/div[3]/div',
                               '//*[@id="i60"]/div[3]/div'
                               ]
        radio_selection(web, stay_up_late_for_videogames_choice, '//*[@id="i57"]/div[3]/div')
        # time.sleep(1)
        # new_info_about_hobbies_choice
        print("new info about hobbies")
        new_info_about_hobbies_choice = ['//*[@id="i67"]/div[3]/div',
                               '//*[@id="i70"]/div[3]/div',
                               '//*[@id="i73"]/div[3]/div',
                               '//*[@id="i76"]/div[3]/div',
                               '//*[@id="i79"]/div[3]/div'
                               ]
        radio_selection(web, new_info_about_hobbies_choice, '//*[@id="i67"]/div[3]/div')
        # time.sleep(1)
        # new_info_about_schoolwork_choice
        print("new info about schoolwork choice")
        new_info_about_schoolwork_choice = ['//*[@id="i86"]/div[3]/div',
                               '//*[@id="i89"]/div[3]/div',
                               '//*[@id="i92"]/div[3]/div',
                               '//*[@id="i95"]/div[3]/div',
                               '//*[@id="i98"]/div[3]/div'
                               ]
        radio_selection(web, new_info_about_schoolwork_choice, '//*[@id="i86"]/div[3]/div')
        # time.sleep(1)
        # new_info_about_schoolwork_friends_choice
        print("new info about schoolwork friends choice")
        new_info_about_schoolwork_friends_choice = ['//*[@id="i105"]/div[3]/div',
                                                    '//*[@id="i108"]/div[3]/div',
                                                    '//*[@id="i111"]/div[3]/div',
                                                    '//*[@id="i114"]/div[3]/div',
                                                    '//*[@id="i117"]/div[3]/div'
                                                    ]
        radio_selection(web, new_info_about_schoolwork_friends_choice, '//*[@id="i105"]/div[3]/div')
        # time.sleep(1)
        # gaming_important_hobby_choice
        print("gaming important hobby choice")
        gaming_important_hobby_choice = ['//*[@id="i124"]/div[3]/div',
                               '//*[@id="i127"]/div[3]/div',
                               '//*[@id="i130"]/div[3]/div',
                               '//*[@id="i133"]/div[3]/div',
                               '//*[@id="i136"]/div[3]/div'
                               ]
        radio_selection(web, gaming_important_hobby_choice, '//*[@id="i124"]/div[3]/div')
        # time.sleep(1)
        # time_spent_online_choice
        print("time_spent_online_choice")
        time_spent_online(web)
        # time.sleep(1)
        # next button
        submit_next_button(web,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
        # waiting 2 seconds for the form to render properly
        time.sleep(2)
        # type_of_learner_choice
        print("type of learner")
        type_of_learner_choice = ['//*[@id="i5"]/div[3]/div',
                                         '//*[@id="i8"]/div[3]/div',
                                         '//*[@id="i11"]/div[3]/div',
                                         '//*[@id="i14"]/div[3]/div',
                                         ]
        radio_selection(web, type_of_learner_choice, '//*[@id="i124"]/div[3]/div')
        # time.sleep(1)
        # time_spent_on_homework_everyday_choice
        print("time spent on homework everyday")
        time_spent_on_homework_everyday_choice = ['//*[@id="i21"]/div[3]/div',
                                  '//*[@id="i24"]/div[3]/div',
                                  '//*[@id="i27"]/div[3]/div',
                                  '//*[@id="i30"]/div[3]/div',
                                  '//*[@id="i33"]/div[3]/div'
                                  ]
        radio_selection(web, time_spent_on_homework_everyday_choice, '//*[@id="i21"]/div[3]/div')
        # time.sleep(1)
        # participate_during_classes_choice
        print("participate during classes")
        participate_during_classes_choice = ['//*[@id="i43"]/div[3]/div',
                                                  '//*[@id="i46"]/div[3]/div',
                                                  '//*[@id="i49"]/div[3]/div',
                                                  ]
        radio_selection(web, participate_during_classes_choice, '//*[@id="i43"]/div[3]/div')
        # time.sleep(1)
        # satisfied_with_technology_choices
        print("satisfied with technology")
        satisfied_with_technology_choices = ['//*[@id="i56"]/div[3]/div',
                                             '//*[@id="i59"]/div[3]/div',
                                             '//*[@id="i62"]/div[3]/div',
                                             ]
        radio_selection(web, satisfied_with_technology_choices, '//*[@id="i56"]/div[3]/div')
        # time.sleep(1)
        # remote_learning_face_to_face_communication_choices
        print("remote learning face to face communication")
        remote_learning_face_to_face_communication_choices = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div',
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div',
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div',
                                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div',
                                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div'
                                             ]
        radio_selection(web, remote_learning_face_to_face_communication_choices, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div')
        # time.sleep(1)
        # talk_to_classmates_choices
        print("talk to classmates")
        talk_to_classmates_choices = ['//*[@id="i73"]/div[3]/div',
                                             '//*[@id="i76"]/div[3]/div',
                                             '//*[@id="i79"]/div[3]/div',
                                                              '//*[@id="i82"]/div[3]/div'
                                             ]
        radio_selection(web, talk_to_classmates_choices, '//*[@id="i73"]/div[3]/div')
        # time.sleep(1)
        # tabs_devices
        print("tabs devices")
        tabs_devices = ['//*[@id="i89"]/div[3]/div',
                                      '//*[@id="i92"]/div[3]/div',
                                      '//*[@id="i95"]/div[3]/div',
                                      '//*[@id="i98"]/div[3]/div'
                                      ]
        radio_selection(web, tabs_devices, '//*[@id="i95"]/div[3]/div')
        # time.sleep(1)
        # discussion_with_teacher_choices
        print("1 to 1 discussion with teacher")
        discussion_with_teacher_choices = ['//*[@id="i105"]/div[3]/div',
                                      '//*[@id="i108"]/div[3]/div',
                                      '//*[@id="i111"]/div[3]/div',
                                      '//*[@id="i114"]/div[3]/div'
                                      ]
        radio_selection(web, discussion_with_teacher_choices, '//*[@id="i89"]/div[3]/div')
        # time.sleep(1)
        # what_factors_lead_to_distraction
        print("What factors lead to distraction")
        factors_lead_to_distraction = ['//*[@id="i122"]/div[2]',
                                           '//*[@id="i125"]/div[2]',
                                           '//*[@id="i128"]/div[2]',
                                           '//*[@id="i131"]/div[2]',
                                           '//*[@id="i134"]/div[2]',
                                           '//*[@id="i137"]/div[2]',
                                           '//*[@id="i140"]/div[2]',
                                           '//*[@id="i143"]/div[2]'
                                           ]
        radio_selection(web, factors_lead_to_distraction, '//*[@id="i122"]/div[2]')
        # time.sleep(1)
        # how_do_these_distraction_affect_you
        print("How do these distraction affect you")
        how_do_these_distraction_affect_you = ['//*[@id="i154"]/div[2]',
                                       '//*[@id="i157"]/div[2]',
                                       '//*[@id="i160"]/div[2]',
                                       '//*[@id="i163"]/div[2]',
                                       '//*[@id="i166"]/div[2]',

                                       ]
        radio_selection(web, how_do_these_distraction_affect_you, '//*[@id="i154"]/div[2]')
        # time.sleep(1)
        # next button
        submit_next_button(web, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
        # waiting 2 seconds for the form to render properly
        time.sleep(2)
        # next button
        submit_next_button(web, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        # waiting 2 seconds for the form to render properly
        time.sleep(2)

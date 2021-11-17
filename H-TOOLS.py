import os
print("""\033[1;36;40m
 █████   █████            ███████████    ███████       ███████    █████        █████████ 
░░███   ░░███            ░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███        ███░░░░░███
 ░███    ░███            ░   ░███  ░  ███     ░░███ ███     ░░███ ░███       ░███    ░░░ 
 ░███████████  ██████████    ░███    ░███      ░███░███      ░███ ░███       ░░█████████   
 ░███░░░░░███ ░░░░░░░░░░     ░███    ░███      ░███░███      ░███ ░███        ░░░░░░░░███  
 ░███    ░███                ░███    ░░███     ███ ░░███     ███  ░███      █ ███    ░███   
 █████   █████               █████    ░░░███████░   ░░░███████░   ███████████░░█████████ 
░░░░░   ░░░░░               ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░░  



\033[1;33;40m @nouredine_kn \033[1;34;40m
\033[1;33;40mt.me/nkcp_tm  \033[1;34;40m
\033[1;33;40m DEV---> NOUREDINE KAOINE \033[1;34;40m
\033[1;33;40m </> PYTHON\033[1;36;40m


""")

print('''
\033[0;37;40m[\033[1;31;40m1\033[0;37;40m] - FIND SITE ADIMN 
\033[0;37;40m[\033[1;31;40m2\033[0;37;40m] -CLEAN LINKS
''')
pp= int(input("\033[0;37;40m[\033[1;31;40m!\033[0;37;40m] \033[1;36;40m ENTRE 1/2 >>>>  "))
os.system('clear')
os.system("cls")
if pp==1:
    import requests, re

    print('''\033[1;34;40m
    ███╗   ██╗ ██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ██╗███╗   ██╗███████╗
    ████╗  ██║██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗██║████╗  ██║██╔════╝
    ██╔██╗ ██║██║   ██║██║   ██║██████╔╝█████╗  ██║  ██║██║██╔██╗ ██║█████╗  
    ██║╚██╗██║██║   ██║██║   ██║██╔══██╗██╔══╝  ██║  ██║██║██║╚██╗██║██╔══╝  
    ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║███████╗██████╔╝██║██║ ╚████║███████╗
    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
             █████╗ ██████╗ ███╗   ███╗███╗   ██╗      ███████╗██████╗       
            ██╔══██╗██╔══██╗████╗ ████║████╗  ██║      ██╔════╝██╔══██╗      
            ███████║██║  ██║██╔████╔██║██╔██╗ ██║█████╗█████╗  ██║  ██║    
            ██╔══██║██║  ██║██║╚██╔╝██║██║╚██╗██║╚════╝██╔══╝  ██║  ██║     
            ██║  ██║██████╔╝██║ ╚═╝ ██║██║ ╚████║      ██║     ██████╔╝    
            ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝      ╚═╝     ╚═════╝    
            
            \033[1;33;40m @nouredine_kn \033[1;34;40m
            \033[1;33;40mt.me/nkcp_tm \033[1;34;40m
            \033[1;33;40m DEV---> NOUREDINE KAOINE \033[1;34;40m
             \033[1;33;40m </> PYTHON\033[1;34;40m
            
            

    ''')

    print("""\033[1;35;40m
    -----------------------------------------------------------------------------------------------------------
    ------------------->[\033[1;31;40m lIKE \033[1;37;40m  www.example.com 
    """)
    url_i = str(input("\033[1;37;40m \033[0;37;40m[\033[1;31;40m!\033[0;37;40m] \033[1;36;40m ENTRE YOUR SITE >>>>\t"))

    print(""" "\033[1;35;40m
    ------------------------------------------------------------------------------------------------------------
    \033[0;37;40m[\033[1;31;40m1\033[0;37;40m] - ASP
    \033[0;37;40m[\033[1;31;40m2\033[0;37;40m] - PHP
    \033[0;37;40m[\033[1;31;40m3\033[0;37;40m] - WORDPRESS
    \033[0;37;40m[\033[1;31;40m4\033[0;37;40m] - DJANGO
    ------------------------------------------------------------------------------------------------------------
    """)
    k = int(input("\033[0;37;40m[\033[1;31;40m!\033[0;37;40m] \033[1;36;40m number of your  site is >>>>  "))
    if k == 1:
        list = ['_admin/', 'backoffice/', 'admin/', 'administrator/', 'moderator/', 'webadmin/', 'adminarea/',
                'bb-admin/',
                'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
                'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp',
                'admin/login.asp', 'admin/admin.asp',
                'admin_area/admin.asp', 'admin_area/login.asp', 'admin/account.html', 'admin/index.html',
                'admin/login.html', 'admin/admin.html',
                'admin_area/admin.html', 'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp',
                'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp',
                'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html',
                'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html',
                'administrator/index.html', 'administrator/login.html', 'administrator/account.html',
                'administrator.html',
                'login.html', 'modelsearch/login.html', 'moderator.html',
                'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html',
                'admincontrol.html',
                'admin_login.html', 'panel-administracion/login.html',
                'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp',
                'admin/admin-login.asp', 'admin-login.asp', 'admin/cp.asp', 'cp.asp',
                'administrator/account.asp', 'administrator.asp', 'login.asp', 'modelsearch/login.asp', 'moderator.asp',
                'moderator/login.asp', 'administrator/login.asp',
                'moderator/admin.asp', 'controlpanel.asp', 'admin/account.html', 'adminpanel.html', 'webadmin.html',
                'pages/admin/admin-login.html', 'admin/admin-login.html',
                'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'user.asp', 'user.html',
                'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
                'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
                'adminarea/index.html',
                'adminarea/admin.html', 'adminarea/login.html',
                'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html',
                'modelsearch/admin.html', 'admin/admin_login.html',
                'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'admin/account.asp',
                'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp',
                'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 'admin_login.asp',
                'panel-administracion/login.asp', 'adminLogin.asp',
                'admin/adminLogin.asp', 'home.asp', 'admin.asp', 'adminarea/index.asp', 'adminarea/admin.asp',
                'adminarea/login.asp', 'admin-login.html',
                'panel-administracion/index.asp', 'panel-administracion/admin.asp', 'modelsearch/index.asp',
                'modelsearch/admin.asp', 'administrator/index.asp',
                'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp',
                'admin2/index.asp', 'adm/index.asp',
                'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp',
                'siteadmin/login.asp', 'siteadmin/index.asp', 'siteadmin/login.html'
            , 'cpanel']
        i = 0
        while i <= 139:
            url = "http://" + url_i + '/' + list[i]
            r = requests.get(url).status_code
            o = open('../admin_asp.txt', 'w')

            if r == 200:
                print("\033[1;32;40mFOND--->  " + url)
                o.write(url + '\n')
            else:
                print("\033[1;31;40mNOT FOND ---->  " + url)

            i += 1
    elif k == 2:
        list = ['_admin/', 'backoffice/', 'admin/', 'administrator/', 'moderator/', 'webadmin/', 'adminarea/',
                'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
                'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php',
                'admin/login.php', 'admin/admin.php', 'admin/account.php',
                'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php',
                'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html',
                'admin/admin.html',
                'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php',
                'admin/home.php', 'admin_area/login.html', 'admin_area/index.html',
                'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
                'admin/account.html', 'adminpanel.html', 'webadmin.html',
                'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html',
                'admin_login.html', 'panel-administracion/login.html',
                'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php',
                'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
                'administrator/account.php', 'administrator.php', 'admin_area/admin.html',
                'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php',
                'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html', 'login.php',
                'modelsearch/login.php', 'moderator.php', 'moderator/login.php',
                'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html',
                'admin-login.html', 'controlpanel.php', 'admincontrol.php',
                'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
                'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html',
                'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html',
                'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html',
                'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
                'administrator.html', 'login.html', 'modelsearch/login.html',
                'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
                'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
                'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php',
                'account.html', 'controlpanel.html', 'admincontrol.html',
                'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php',
                'admin.php', 'adminarea/index.php',
                'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php',
                'panel-administracion/admin.php', 'modelsearch/index.php',
                'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php',
                'admin2.php', 'admin2/login.php', 'admin2/index.php',
                'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php',
                'administratorlogin.php', 'phpmyadmin']
        i = 0
        while i <= 145:
            url = "http://" + url_i + '/' + list[i]
            r = requests.get(url).status_code
            o = open('../admin_php.txt', 'w')
            if r == 200:
                print("\033[1;32;40mFOND----> " + url)
                o.write(url)
            else:
                print("\033[1;31;40mNOT FOND ----> " + url)
            i += 1
    elif k == 3:
        list = ['wp-admin/', 'wp-login']
        i = 0
        while i <= 2:
            url = "http://" + url_i + '/' + list[i]
            r = requests.get(url)
            o = open('admin_wp.txt', 'w')
            if r.status_code == 200:
                print("\033[1;32;40mFOND----> " + url)
                o.write(url + '\n')
            else:
                print("\033[1;31;40mNOT FOND----> " + url)
            i += 1
    elif k == 4:
        list = ['admin/', 'django-admin']
        i = 0
        while i <= 2:
            url = "http://" + url_i + '/' + list[i]
            r = requests.get(url)
            o = open('admin_dj.txt', 'w')
            if r.status_code == 200:
                print("\033[1;32;40mFOND----> " + url)
                o.write(url + '\n')
            else:
                print("\033[1;31;40mNOT FOND ----> " + url)
            i += 1


elif pp==2:
    import requests, re

    print(""" \033[1;34;40m
      █████████  █████       ██████████   █████████   ██████   █████           █████       █████ ██████   █████ █████   ████  █████████ 
      ███░░░░░███░░███       ░░███░░░░░█  ███░░░░░███ ░░██████ ░░███           ░░███       ░░███ ░░██████ ░░███ ░░███   ███░  ███░░░░░███ 
     ███     ░░░  ░███        ░███  █ ░  ░███    ░███  ░███░███ ░███            ░███        ░███  ░███░███ ░███  ░███  ███   ░███    ░░░  
    ░███          ░███        ░██████    ░███████████  ░███░░███░███            ░███        ░███  ░███░░███░███  ░███████    ░░█████████  
    ░███          ░███        ░███░░█    ░███░░░░░███  ░███ ░░██████            ░███        ░███  ░███ ░░██████  ░███░░███    ░░░░░░░░███   
    ░░███     ███ ░███      █ ░███ ░   █ ░███    ░███  ░███  ░░█████            ░███      █ ░███  ░███  ░░█████  ░███ ░░███   ███    ░███
     ░░█████████  ███████████ ██████████ █████   █████ █████  ░░█████ █████████ ███████████ █████ █████  ░░█████ █████ ░░████░░█████████ 
    
      ░░░░░░░░░  ░░░░░░░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░ ░░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░   ░░░░  ░░░░░░░░░  
   \033[1;33;40m @nouredine_kn \033[1;34;40m
    \033[1;33;40mt.me/nkcp_tm \033[1;34;40m
    \033[1;33;40m DEV---> NOUREDINE KAOINE \033[1;34;40m
    \033[1;33;40m </> PYTHON\033[1;34;40m
    
   
   
   \033[1;35;40m
      """)
    w = "url.txt"
    url = open(w, "r").read().splitlines()
    o = open("urls_clinks.txt", "w")
    for line in url:
        url2 = line.split("//")[1]
        url3 = "www." + url2.split("/")[0] + "\n"
        print("------->" + url3 + "\033[1;32;40mDONE\n")
        o.write(url3)




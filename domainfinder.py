from tkinter import *


def display_names():
    output = search(entry_name.get().split())
    if output == "Nothing was found":
        label_output = Label(root, text=output)
        label_output.pack()

    else:
        for item in output:
            label_output = Label(root, text=item)
            label_output.pack()

    label_output = Label(root, text="---------------")
    label_output.pack()


def search(full_name):

    researched = []
    for i in range(len(full_name)):
        researched.append([])

    i = 0
    for name in full_name:
        for domain in domains:
            if name[-len(domain)::] == domain and len(name) > len(domain):
                researched[i].append(domain)
        i += 1
    del(i)

    found_list = []
    for j in range(len(full_name)):
        for item in researched[j]:
            found_list.append(f"{full_name[j][:-len(item):]}.{item}")

    if len(found_list) == 0:
        return "Nothing was found"
    else:
        return found_list


domains = "no .fr .ee .cz .by .it .me .dk .ie .es .lt .lv .de .pl .eu .ro .be .fi .gr .pt .se .si .ch .mk .is .ge .nl .at .ba .ua .mc .ad .md .bg .gg .gi .li .sk .uk .al .im .pm .sm .fo .hr .rs .yt .hu .lu .ax .sx .ac .je .re .in .ru .cn .kz .su .la .qa .sa .id .ae .ye .af .kg .sg .bh .ph .th .tj .hk .lk .pk .tl .am .mm .om .tm .mn .vn .jo .jp .iq .kr .ps .bt .mv .kw .tw .my .sy .az .cx .us .ai .gl .ky .ca .pa .bb .lc .tc .vc .gd .ag .vg .ni .vi .bm .dm .hn .kn .do .cr .pr .bs .gt .ht .tt .cu .gu .sv .mx .bz .sc .dj .ml .sl .cm .gm .km .gn .sn .tn .ao .ga .ma .na .cd .sd .td .ke .ne .bf .cf .cg .eg .mg .ng .tg .ug .eh .gh .sh .bi .ci .bj .io .so .gq .er .lr .mr .ls .et .st .mu .cv .bw .gw .mw .rw .zw .ly .dz .mz .sz .tz .za .co .gf .tf .as .ec .pe .cl .bo .gp .mq .sr .gs .cw .gy .uy .ws .tv .cc .fm .to .wf .pf .mh .tk .nr .nu .pw .nc .nf .ki .hm .vu .nz .pn .mp .name .delivery .abogado .rip .wedding .forsale .work .casa .world .frl .click .help .sarl .gifts .top .ong .auction .ngo .lgbt .club .today .media .moda .shoes .gdn .lotto .biz .energy .business .ltda .forex .loan .tickets .jewelry .broker .taxi .law .spreadbetting .bet .boats .agency .company .solar .shop .ltd .promo .mobi .com .org .srl .bible .group .vip .mom .net .link .blog .show .football .tennis .cricket .yoga .soccer .golf .racing .team .run .hockey .ski .motorcycles .fyi .bingo .chat .design .one .fit .flowers .sale .video .garden .memorial .legal .money .coach .band .coupons .sucks .gold .plus .date .faith .review .love .express .lol .earth .cloud .live .studio .cfd .family .security .protection .pet .plumbing .salon .apartments .immo .property .rent .amsterdam .osaka .sydney .wales .gent .nrw .taipei .miami .corsica .kyoto .istanbul .tires .cars .auto .parts .adult .porn .sex .xxx .irish .alsace .lat .swiss .theater .theatre .casino .party .poker .movie .fans .win .dog .men .game .green .life .games .pizza .diet .restaurant .cafe .vin .wine .healthcare .doctor"
domains = domains.split(" .")


root = Tk()
root.title("Name extension finder")

label_title = Label(root, text="Your name:")
label_title.pack()

entry_name = Entry(root, width=50)
entry_name.pack()

button_run = Button(root, text="Search", command=display_names)
button_run.pack()

root.mainloop()

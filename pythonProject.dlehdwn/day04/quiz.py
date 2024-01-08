# # 대문자로 변형
# a = str(input("소문자로 입력해 주세요 : "))
# print(a.upper())

# 노래가사에서 단어 카운트
b = """Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (no, I don't know how)
How to erase your body from out my brain (what you gon' do now?)
Maybe I should just focus on me instead (but all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're goin' 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (someone tell me how)
How much more do I gotta drink for the pain (what you gon' do now?)
You did things to me that I just can't forget (now all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're going 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (of my mind)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Did you know you're the one that got away?
And even now, baby, I'm still not okay
Did you know that my dreams, they're all the same
Every time I close my eyes?
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
(Whoa)
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)"""
print(f"가사에서 right는 {b.count('right')}개, left는 {b.count('left')}개 나옵니다 ")
print(f"가사의 길이는 {len(b)}")


# 뉴스 기사를 리스트화
article = """The US aviation regulator has said 171 Boeing 737 Max 9 planes will remain grounded until it is satisfied the planes are safe.

The Federal Aviation Administration (FAA) has been inspecting the jets after part of an Alaska Airlines plane's fuselage fell off on Friday.

The FAA said its first priority was "keeping the flying public safe".

Boeing's CEO Dave Calhoun told staff that its response "is and must be" the focus of the company.

Thousands of passengers saw their flights cancelled after major US airlines grounded dozens of the jets.

"We have grounded the affected airplanes, and they will remain grounded until the FAA is satisfied that they are safe," the FAA said in a statement on Sunday.

Boeing also said that it will hold an all-employee meeting about safety on Tuesday to address its response to the incident.

"When serious accidents like this occur, it is critical for us to work transparently with our customers and regulators to understand and address the causes of the event, and to ensure they don't happen again," Mr Calhoun said.

Disruptions have primarily affected flights in the US.

The vast majority of Boeing 737 Max 9s used in the US are operated by United Airlines and Alaska, while Turkish Airlines, Panama's Copa Airlines and Aeromexico have also grounded jets of the same model for inspections.

Alaska grounded 65 planes, and said on Sunday that it had cancelled 163 flights, or 21%. Around 25,000 people were affected. The airline said travel disruptions from the grounding of some of its planes is expected to last until at least mid-week.United has grounded 79 planes, and said on Sunday it had cancelled about 180 flights.

Meanwhile, authorities are still searching for the plug door - which they believe fell to the ground in the western suburbs of Portland - and have appealed to the public to help find the panel.

During Friday's incident, Alaska Airlines flight 1282 from Portland, Oregon, to Ontario, California, reached 16,000ft (4,876m) when it began an emergency descent, according to flight tracking data.

Passengers on board said a large section of the plane's outer shell fell to the ground shortly after take-off."""
newarticle = article.replace('after','before').replace('it','🤣').split()
print(newarticle)




# using joy library

background = rectangle(w = 300,h = 300, fill = "#11B700")
outerCircle1 = circle(r = 150,fill = "#FF00CE")
outerCircle2 = circle(r = 120, fill = "#00E8F8")
outerCircle3 = circle(r = 105, fill = "#11D3FF", stroke = "none")
outerCircle4 = circle(r = 90, fill = "#00B2FF", stroke = "none")
outerCircle5 = circle(r = 80, fill = "#009CFF", stroke = "none")
outercircle6 = circle(r = 125, fill = "#FFCA00", stroke = "none")

innerCircle1 = circle(r = 70, fill = "#DA03FF")
floCir = circle(r=6, x=0, y= 95, fill = "white", stroke = "none") | repeat(12, rotate(30))
p = circle(r = 3,x = 0,y = 95, fill = "black") | repeat(12, rotate(30))
poi1 = point(x = 0, y=108)
poi2 = point(x = 13,y = 95)
poi3 = point(x= 0, y = 82)
poi4 = point(x = -13, y = 95)
p1 = point(x = 0, y=115)
p2 = point(x = 20,y = 95)
p3 = point(x= 0, y = 75)
p4 = point(x = -20, y = 95)
p21 = point(x = 0,y = 150)
p22 = point(x = 150,y = 0)
p23 = point(x = 0, y = -150)
p24 = point( x = -150, y= 0)
rhombus0 = polygon([p21,p22,p23,p24], fill = "#FFFB00", stroke = "none") | repeat(12, rotate(30))
rhombus1 = polygon([poi1,poi2,poi3,poi4], fill= "#41FF03 ", stroke = "none") | repeat(12, rotate(30))
rhombus2 = polygon([p1,p2,p3,p4], fill = "#FF5733" ) | repeat(12, rotate(30))
lin = line(x1 = 0, y1=70, x2 = 0,y2 = 120) | repeat(18, rotate(20) )
p11 = point(x = 0,y = 70)
p12 = point(x = 70, y = 0)
p13 = point(x = 0, y = -70)
p14 = point(x = -70, y= 0)
rhombus3 = polygon([p11,p12,p13,p14], fill = "white", stroke = "none") | repeat(12, rotate(30))
innerCircle2 = circle(r=50, fill = "yellow", stroke = "none")
innerCircle3 = circle(r = 55, fill = "#FCDCFF", stroke = "none")
eli = ellipse(h = 80,w = 40) | repeat(18, rotate(20))
def genLine(n):
    b = line(x1 = 0,y1 = 0, x2 = 2,y2 = 0)
    for i in range(n):
        x = random(-150,150)
        y = random(-150,150)
        a = line(x1 = x,y1 = y,x2 = x+3,y2 = y, stroke = "#064300", stroke_width = "1.5")
        b=b+a
    return b
                 
def generateCircle(n):
    # b = circle(r = 3)
    b = line(x1 = 0,y1 = 0, x2 = 5,y2 = 5)
    for i in range(n):
        a = line(x1 = random(-19,19),y1 = random(-19,19),x2 = random(-19,19),y2 = random(-19,19), stroke =  color(r = random(255), g = random(255), b = random(255), a= 0.5))
        # a = circle(r = random(4),x= random(-16,16), y= random(-16,16), fill = color(r = random(255), g = random(255), b = random(255), a= 0.5), stroke = "none")
        b=b+a
    return b


show(background,genLine(250),outerCircle1,rhombus0,outercircle6, outerCircle2,outerCircle3, outerCircle4, outerCircle5,innerCircle1,rhombus2, rhombus1,floCir,rhombus3,innerCircle3, innerCircle2,eli, generateCircle(300), p )

def gradegg():
    marksTmp=raw_input('input marks (0~100)')
    g=int(marksTmp)
    if 90<=g<=100:
        print ("A")
    if 80<=g<90:
        print ("B")
    if 70<=g<80:
        print ("C")
    if 60<=g<70:
        print ("D")
    if g<60:
        print ("F")

gradegg()


name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #in inches
weight = 180 #in pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = height * 2.54
weight_in_kilograms = weight / 2.205

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("When he's in London, he is %d centimetres tall. Wow." % height_in_cm)
print("He's %d pounds heavy." % weight)
print("Actually, that's not too heavy.")
print("In London, he sounds lighter, as he weighs %d kilograms." % weight_in_kilograms)
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

print("If I add %d, %d, and %d, I get %d." %(
    age, height, weight, age + height + weight))


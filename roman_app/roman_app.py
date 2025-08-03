def to_roman(number):
    onluklar = [
        "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"
    ]
    birlikler = [
        "","I","II","III","IV","V","VI","VII","VIII","IX"
    ]
    
    return (
        onluklar[number//10]+
        birlikler[(number%10)]
    )

sayi = int(input("Bir sayı gir:"))
print(f"Roman Rakamı: {to_roman(sayi)}")
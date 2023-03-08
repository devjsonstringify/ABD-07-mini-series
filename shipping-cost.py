unitsDictionary = {
	"grams": "g",
	"kilogram": "kg",
}

penDictionary = {
	"weight": 17,
	"cost": 3,
	"penPerPack": 12,
	"weightOfPenPerPack": 0,
	"unit": unitsDictionary["grams"]
}

boxDictionary = {
	"weight": 20,
	"weightPerPack": 0,
	"unit": unitsDictionary["kilogram"],
	"boxes_count": 500,
	"boxes_cost": 0,
	"cost_of_pen_of_packs": 0,
}

shippingDictionary = {
	"costPerKg": 0.50,
	"totalCost": 0
}
calculate_weight_of_pen_per_pack = penDictionary["weight"] * penDictionary["penPerPack"]
penDictionary['weightOfPenPerPack'] = calculate_weight_of_pen_per_pack

calculate_number_of_pen_on_box = 98
boxDictionary["weightPerPack"] = calculate_number_of_pen_on_box

calculate_boxes_count = boxDictionary["boxes_count"] / calculate_number_of_pen_on_box
boxDictionary["boxes_cost"] = calculate_boxes_count

calculate_pen_in_a_pack = boxDictionary["boxes_count"] * penDictionary["cost"]
boxDictionary["cost_of_pen_of_packs"] = calculate_pen_in_a_pack

calculate_shipping_total_cost = 1000 * shippingDictionary["costPerKg"]
shippingDictionary["totalCost"] = calculate_shipping_total_cost

total_shipping_cost_of_one_ton = boxDictionary["cost_of_pen_of_packs"] + boxDictionary["boxes_count"]

print(f'The cost of 1 ton of pens ${total_shipping_cost_of_one_ton}')

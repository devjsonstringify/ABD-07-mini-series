UNITS = {
	"grams": "g",
	"kilogram": "kg",
}

penDict = {
	"weight": 17,
	"cost": 3,
	"penPerPack": 12,
	"weightOfPenPerPack": 0,
	"unit": UNITS["grams"]
}

boxDict = {
	"weight": 20,
	"weightPerPack": 0,
	"unit": UNITS["kilogram"],
	"boxes_count": 500,
	"boxes_cost": 0,
	"cost_of_pen_of_packs": 0,
}

shippingDic = {
	"costPerKg": 0.50,
	"totalCost": 0
}
calc_weight_of_pen_per_pack = penDict["weight"] * penDict["penPerPack"]
penDict['weightOfPenPerPack'] = calc_weight_of_pen_per_pack

formatted_number = "0."+str(penDict["weightOfPenPerPack"])
calc_weight_per_pack = int(boxDict["weight"] / float(formatted_number))
boxDict["weightPerPack"] = calc_weight_per_pack

calc_boxes_count = boxDict["boxes_count"] / calc_weight_per_pack
boxDict["boxes_cost"] = calc_boxes_count

calc_cost_of_pen_of_packs = boxDict["boxes_count"] * penDict["cost"]
boxDict["cost_of_pen_of_packs"] = calc_cost_of_pen_of_packs

calc_total_cost = 1000 * shippingDic["costPerKg"]
shippingDic["totalCost"] = calc_total_cost

shipping_overall_cost = boxDict["cost_of_pen_of_packs"] + boxDict["boxes_count"]

print(f'The cost of 1 ton of pens ${shipping_overall_cost}')

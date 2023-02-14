#include <iostream>


int main()
{

	bool isRedirect = false;
	bool isCompletedHealthRequirements = false;
	bool isFlightCompleted = false;
	char getUserFlightB12Status;
	char getUserTemperatureAnswer;
  std::sting redirectMessage = "Air-traffic-controller: we are redirecting you to nearby airport.: ";

	while (isRedirect == false && isFlightCompleted == false) {

		std::cout << "Air-traffic-controller: Is flight B12 is takeoff already? [y/n]: ";
		std::cin >> getUserFlightB12Status;

		if (getUserFlightB12Status == 'n') {
			std::cout << redirectMessage;
			isRedirect = true;
		}
		else {
			std::cout << "Air-traffic-controller: is current weather is between -35 to -55? [y/n]: ";
			std::cin >> getUserTemperatureAnswer;
			
			if (getUserTemperatureAnswer == 'n') {
				std::cout << redirectMessage;
				isRedirect = true;
			}else {
			std::cout << "Air-traffic-controller: Is flight A12 completed covid-19 health requirements? [y/n]: ";
			std::cin >> isCompletedHealthRequirements;

			if (isCompletedHealthRequirements == 'no') {
				std::cout << redirectMessage;
				isRedirect = true;
			}else {
				std::cout << "Air-traffic-controller: Please proceed to gate 12";
				isFlightCompleted = true;
				}
			}
		}

	}

}

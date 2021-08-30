from map.campaign import SafetyFeatures, Testimonials, Innovation, Models, TopPanel, TopPanelOptions, Cookies


class PageMap:
    '''Page Map class

        - The class is used to wire/map the locators in each page to the corresponding feature steps.
        - It is implemented using Python dictionary action_map
        - For each element there is a key, to identify the locator type for promoting action reuse.
        - While adding/updating any keys in this class, the convention is to use the following order :
            App:Page:Element:Locator
        '''

    action_map ={'Campaign page':
            {'Cookies alert':{
                'Heading': {'locator': Cookies.header, 'type': "xpath"},
                'Accept': {'locator': Cookies.accept, 'type': "xpath"},},
            'Safety Section': {
                'Heading': {'locator': SafetyFeatures.header, 'type': "xpath"},
                'Safety header': {'locator': SafetyFeatures.safety_header, 'type': "xpath"},
                'Safety video': {'locator': SafetyFeatures.safety_video, 'type': "xpath"},
                'Speed section header': {'locator': SafetyFeatures.speed_header, 'type': "xpath"},
                'Speed cap': {'locator': SafetyFeatures.speed_cap, 'type': "xpath"},
                'Highway pilot': {'locator': SafetyFeatures.highway_pilot, 'type': "xpath"},
                'Driver monitoring cameras': {'locator': SafetyFeatures.driver_monitor, 'type': "xpath"},
                'Care key': {'locator': SafetyFeatures.care_key, 'type': "xpath"},
                'Learn more URL': {'locator': SafetyFeatures.learn_more, 'type': "xpath"},
                'Conditions message': {'locator': SafetyFeatures.conditions, 'type': "xpath"},},
            'Testimonial Section': {
                'Heading': {'locator': Testimonials.header, 'type': "xpath"},
                'Testimonial header': {'locator': Testimonials.tesimonial_header, 'type': "xpath"},
                'Testimonial description': {'locator': Testimonials.testomonial_description, 'type': "xpath"},
                'Amy Video': {'locator': Testimonials.amy_video, 'type': "xpath"},
                'Amy': {'locator': Testimonials.amy, 'type': "xpath"},
                'Amy Description': {'locator': Testimonials.amy_description, 'type': "xpath"},},
            'Innovation Section': {
                'Heading': {'locator': Innovation.header, 'type': "xpath"},
                'Innovation header': {'locator': Innovation.innovation_header, 'type': "xpath"},
                'Innovation description': {'locator': Innovation.innovation_description, 'type': "xpath"},
                'Learn more URL': {'locator': Innovation.learn_more, 'type': "xpath"},
                'Innovation image': {'locator': Innovation.innovation_image, 'type': "xpath"},},
            'Models Section': {
                'Heading': {'locator': Models.header, 'type': "xpath"},
                'Models Header': {'locator': Models.models_header, 'type': "xpath"},
                'XC90 SUV Header': {'locator': Models.xc_90_header, 'type': "xpath"},
                'XC90': {'locator': Models.xc_90, 'type': "xpath"},
                'XC90 Image': {'locator': Models.xc_90_image, 'type': "xpath"},
                'XC90 Learn': {'locator': Models.xc_90_learn, 'type': "xpath"},
                'XC90 Shop': {'locator': Models.xc_90_shop, 'type': "xpath"},
                'Learn More': {'locator': Models.learn_more, 'type': "xpath"},
                'Mild Hybrid Cars': {'locator': Models.mild_hybrid, 'type': "xpath"},},
            'Top Panel Section': {
                'Heading': {'locator': TopPanel.header, 'type': "xpath"},
                'Volvo logo': {'locator': TopPanel.volvo_logo, 'type': "xpath"},
                'Our Cars URL': {'locator': TopPanel.our_cars, 'type': "xpath"},
                'Options': {'locator': TopPanel.options, 'type': "xpath"},},
            'Top Panel options Section': {
                'Heading': {'locator': TopPanelOptions.header, 'type': "xpath"},
                'Volvo logo': {'locator': TopPanelOptions.volvo_logo, 'type': "xpath"},
                'Buy': {'locator': TopPanelOptions.buy, 'type': "xpath"},
                'Own': {'locator': TopPanelOptions.own, 'type': "xpath"},
                'Why Volvo': {'locator': TopPanelOptions.why_volvo, 'type': "xpath"},
                'Explore': {'locator': TopPanelOptions.explore, 'type': "xpath"},
                'More': {'locator': TopPanelOptions.more, 'type': "xpath"},
                'International': {'locator': TopPanelOptions.international, 'type': "xpath"},
                'Facebook': {'locator': TopPanelOptions.facebook, 'type': "xpath"},},
            'Buy Section': {
                'Heading': {'locator': TopPanelOptions.header, 'type': "xpath"},
                'Purchase Header': {'locator': TopPanelOptions.purchase, 'type': "xpath"},
                'Fleet sales': {'locator': TopPanelOptions.fleet_sales, 'type': "xpath"},
                'Used cars': {'locator': TopPanelOptions.used_sales, 'type': "xpath"},},},}


































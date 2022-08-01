from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/product_line')
def product_line():
    return render_template('product_line.html')


@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/sister_companies')
def sister_companies():
    return render_template('sister_companies.html')

@app.route('/akt')
def akt():
    return render_template('akt.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/termsofuse')
def termsofuse():
    return render_template('termsofuse.html')



# PRODUCT LINE 

@app.route('/lighting_types/airport_lighting')
def airport_lighting():
    return render_template('/lighting_types/airport_lighting.html')

@app.route('/lighting_types/highway_construction_lighting')
def highway_construction_lighting():
    return render_template('/lighting_types/highway_construction_lighting.html')

@app.route('/lighting_types/marine_lighting')
def marine_lighting():
    return render_template('/lighting_types/marine_lighting.html')

@app.route('/lighting_types/railroad_lighting')
def railroad_lighting():
    return render_template('/lighting_types/railroad_lighting.html')



# Marine Lighting 

@app.route('/marine/load_light')
def load_light():
    return render_template('/marine/load_light.html')

@app.route('/marine/barge_light')
def barge_light():
    return render_template('/marine/barge_light.html')

@app.route('/marine/dredge_light')
def dredge_light():
    return render_template('/marine/dredge_light.html')

@app.route('/marine/solar_dredge_light')
def solar_dredge_light():
    return render_template('/marine/solar_dredge_light.html')

@app.route('/marine/pilot_location_light')
def pilot_location_light():
    return render_template('/marine/pilot_location_light.html')

@app.route('/marine/model400_led_mooring_light')
def model400_led_mooring_light():
    return render_template('/marine/model400_led_mooring_light.html')



#AKT

@app.route('/akt/traffic_signal_lenses')
def traffic_signal_lenses():
    return render_template('/akt/traffic_signal_lenses.html')

@app.route('/akt/no18CenterMountDelineator')
def no18CenterMountDelineator():
    return render_template('/akt/no18CenterMountDelineator.html')

@app.route('/akt/567_guardrail_delineator')
def guardrail_delineator():
    return render_template('/akt/567_guardrail_delineator.html')

@app.route('/akt/aluminum_backer')
def aluminum_backer():
    return render_template('/akt/aluminum_backer.html')

@app.route('/akt/181_guardrail_delineator')
def guardrail_delineator_181():
    return render_template('/akt/181_guardrail_delineator.html')

@app.route('/akt/bituminous_pavement_marker_adhesive')
def bituminous_pavement_marker_adhesive():
    return render_template('/akt/bituminous_pavement_marker_adhesive.html')

@app.route('/akt/prismatic_retroreflective_pavement_marker')
def prismatic_retroreflective_pavement_marker():
    return render_template('/akt/prismatic_retroreflective_pavement_marker.html')

@app.route('/akt/concrete_barrier_wall_marker')
def concrete_barrier_wall_marker():
    return render_template('/akt/concrete_barrier_wall_marker')

@app.route('/akt/butyl_pads')
def butyl_pads():
    return render_template('/akt/butyl_pads.html')

@app.route('/akt/model_400_led_pc')
def model_400_led_pc():
    return render_template('/akt/model_400_led_pc.html')


# HIGHWAY LIGHTS

@app.route('/highway/model2006plus_solar_assist')
def model2006plus_solar_assist():
    return render_template('/highway/model2006plus_solar_assist.html')

@app.route('/highway/S_solar_2006')
def S_solar_2006():
    return render_template('/highway/S_solar_2006.html')

@app.route('/highway/model2006')
def model2006():
    return render_template('/highway/model2006.html')

@app.route('/highway/model2006d')
def model2006d():
    return render_template('/highway/model2006d.html')

@app.route('/highway/audible_device_model_400_ADA')
def audible_device_model_400_ADA():
    return render_template('/highway/audible_device_model_400_ADA.html')

@app.route('/highway/model212_3_S_solar_assist')
def model212_3_S_solar_assist():
    return render_template('/highway/model212_3_S_solar_assist.html')

@app.route('/highway/model212_3_solar')
def model212_3_solar():
    return render_template('/highway/model212_3_solar.html')

@app.route('/highway/M212_3LW')
def M212_3LW():
    return render_template('/highway/M212_3LW.html')

@app.route('/highway/LED_PC')
def LED_PC():
    return render_template('/highway/LED_PC.html')

@app.route('/highway/sequential_device')
def sequential_device():
    return render_template('/highway/sequential_device.html')

@app.route('/highway/standaloneflarelight')
def standaloneflarelight():
    return render_template('/highway/standaloneflarelight.html')

@app.route('/highway/strobeseries7400')
def strobeseries7400():
    return render_template('/highway/strobeseries7400.html')

@app.route('/highway/strobeseries7401')
def strobeseries7401():
    return render_template('/highway/strobeseries7401.html')

@app.route('/highway/portable10')
def portable10():
    return render_template('/highway/portable10.html')

@app.route('/highway/portable2')
def portable20():
    return render_template('/highway/portable20.html')

@app.route('/highway/batteryadapter')
def batteryadapter():
    return render_template('/highway/batteryadapter.html')

@app.route('/highway/audible400ml')
def audible400ml():
    return render_template('/highway/audible400ml.html')







# AIRPORT PRODUCTS 

@app.route('/airport/model_630')
def model_630():
    return render_template('/airport/model_630.html')

@app.route('/airport/model_630_solar')
def model_630_solar():
    return render_template('/airport/model_630_solar.html')

@app.route('/airport/model601_solar_airport_light')
def model601_solar_airport_light():
    return render_template('/airport/model601_solar_airport_light.html')


@app.route('/airport/model2006D_Cell_Solar_Assist')
def model2006D_Cell_Solar_Assist():
    return render_template('/airport/model2006D_Cell_Solar_Assist.html')

# RAILROAD PRODUCTS

@app.route('/railroad/blue_flag_light')
def blue_flag_light():
    return render_template('/railroad/blue_flag_light.html')

@app.route('/railroad/blue_flag_strobe_light')
def blue_flag_strobe_light():
    return render_template('/railroad/blue_flag_strobe_light.html')



# REFLECTORS 

@app.route('/reflectors/EBMT')
def EBMT():
    return render_template('/reflectors/EBMT.html')

@app.route('/reflectors/EBM3x4')
def EBM3x4():
    return render_template('/reflectors/EBM3x4.html')

@app.route('/reflectors/GRD-S')
def GRD_S():
    return render_template('/reflectors/GRD-S.html')



# Mounting Brackets 

@app.route('/mounting_brackets/center_mounting_bracket')
def center_mounting_bracket():
    return render_template('/mounting_brackets/center_mounting_bracket.html')

@app.route('/mounting_brackets/ZMountingBracket')
def ZMountingBracket():
    return render_template('/mounting_brackets/ZMountingBracket.html')

@app.route('/mounting_brackets/right_MountingBracket')
def right_MountingBracket():
    return render_template('/mounting_brackets/right_MountingBracket.html')

@app.route('/mounting_brackets/left_MountingBracket')
def left_MountingBracket():
    return render_template('/mounting_brackets/left_MountingBracket.html')

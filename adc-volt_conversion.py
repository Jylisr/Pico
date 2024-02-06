def adc_to_voltage(adc_value, bits, reference_voltage=5.0):
    max_adc_value = 2**bits - 1
    return (adc_value / max_adc_value) * reference_voltage

def voltage_to_adc(voltage, bits, reference_voltage=5.0):
    max_adc_value = 2**bits - 1
    return int((voltage / reference_voltage) * max_adc_value)

adc_value = int(input("Enter ADC value: "))
adc_bits = int(input("Enter number of ADC bits: "))
converted_voltage = adc_to_voltage(adc_value, adc_bits)
print(f"The voltage for ADC value {adc_value} is: {converted_voltage} volts")

voltage = float(input("Enter voltage in volts: "))
adc_bits = int(input("Enter number of ADC bits: "))
converted_adc_value = voltage_to_adc(voltage, adc_bits)
print(f"The ADC value for voltage {voltage} volts is: {converted_adc_value}")

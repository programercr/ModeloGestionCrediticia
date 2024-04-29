Algoritmo ModeloGestionCrediticia
	
    // Menú para seleccionar el tipo de financiamiento
    Mostrar "Seleccione el tipo de financiamiento que desea solicitar:"
    Mostrar "1. Crédito Personal"

    Leer tipo_financiamiento
	
    // Nota para ingresar salario bruto y neto
    Mostrar "Por favor, ingrese su salario bruto y neto."
	
    // Ingreso de información según condición laboral
    Leer tipo_de_trabajo
    Si tipo_de_trabajo es "asalariado" entonces
        Leer salario_bruto, salario_neto
    Sino si tipo_de_trabajo es "independiente" entonces
			Leer ingreso_mensual_promedio
		Fin Si
		
		// Nota para ingresar operaciones reguladas y no reguladas
		Mostrar "Ahora, ingrese sus operaciones crediticias reguladas y no reguladas."
		
		// Ingreso de información sobre cuotas de operaciones crediticias
		Leer cuotas_operaciones_reguladas, cuotas_operaciones_no_reguladas
		
		// Calcular nivel de endeudamiento en porcentaje
		Si tipo_de_trabajo es "asalariado" entonces
			total_deudas = cuotas_operaciones_reguladas + cuotas_operaciones_no_reguladas
			nivel_endeudamiento = (total_deudas * 100) / salario_neto
		Sino si tipo_de_trabajo es "independiente" entonces
				total_deudas = cuotas_operaciones_reguladas + cuotas_operaciones_no_reguladas
				nivel_endeudamiento = (total_deudas * 100) / ingreso_mensual_promedio
			Fin Si
			
			
	FinSi
		
			// Verificar si el nivel de endeudamiento es menor al 50%
			Si nivel_endeudamiento es menor que 50 entonces
				Mostrar "El cliente es sujeto de crédito."
			Sino
				Mostrar "El cliente no es sujeto de crédito debido a su nivel de endeudamiento alto."
			Fin Si
		Finsi	
		Fin Algoritmo

class GymMembershipSystem:
    def __init__(self):
        # Planes de membresía disponibles (nombre, precio, disponibilidad)
        self.membership_plans = {
            "Básico": {"price": 100, "available": True},
            "Estándar": {"price": 150, "available": True},
            "Premium": {"price": 250, "available": True}
        }
        
        # Características adicionales (nombre, precio, disponibilidad, es_premium)
        self.additional_features = {
            "Clases grupales": {"price": 50, "available": True, "premium": False},
            "Entrenador personal": {"price": 120, "available": True, "premium": False},
            "Nutricionista": {"price": 80, "available": True, "premium": False},
            "Acceso a spa": {"price": 90, "available": True, "premium": True},
            "Entrenamientos especializados": {"price": 100, "available": True, "premium": True},
            "Acceso a instalaciones VIP": {"price": 150, "available": True, "premium": True}
        }

    def calculate_total_cost(self, membership_plan, selected_features):
        """Calcula el costo total de la membresía y características seleccionadas"""
        # Verificar que el plan de membresía existe y está disponible
        if membership_plan not in self.membership_plans:
            print(f"Error: El plan de membresía '{membership_plan}' no existe.")
            return -1
        
        if not self.membership_plans[membership_plan]["available"]:
            print(f"Error: El plan de membresía '{membership_plan}' no está disponible.")
            return -1
        
        # Calcular costo base del plan
        base_cost = self.membership_plans[membership_plan]["price"]
        
        # Verificar y calcular el costo de las características adicionales
        features_cost = 0
        has_premium_feature = False
        
        for feature in selected_features:
            if feature not in self.additional_features:
                print(f"Error: La característica '{feature}' no existe.")
                return -1
                
            if not self.additional_features[feature]["available"]:
                print(f"Error: La característica '{feature}' no está disponible.")
                return -1
                
            features_cost += self.additional_features[feature]["price"]
            
            if self.additional_features[feature]["premium"]:
                has_premium_feature = True
        
        # Calcular costo total antes de descuentos y recargos
        total_cost = base_cost + features_cost
        
        # Aplicar descuentos según el costo total
        discount = 0
        if total_cost > 400:
            discount = 50
        elif total_cost > 200:
            discount = 20
        
        # Aplicar recargo por características premium (15%)
        premium_surcharge = 0
        if has_premium_feature:
            premium_surcharge = int(total_cost * 0.15)
        
        # Calcular costo final
        final_cost = total_cost - discount + premium_surcharge
        
        return final_cost, base_cost, features_cost, discount, premium_surcharge

    def process_membership(self):
        """Procesa la selección de membresía del usuario"""
        # Mostrar planes de membresía disponibles
        print("\n=== PLANES DE MEMBRESÍA ===")
        for plan, details in self.membership_plans.items():
            if details["available"]:
                print(f"- {plan}: ${details['price']}")
        
        # Seleccionar plan de membresía
        while True:
            selected_plan = input("\nSeleccione un plan de membresía: ")
            if selected_plan in self.membership_plans and self.membership_plans[selected_plan]["available"]:
                break
            print("Plan no válido o no disponible. Intente nuevamente.")
        
        # Mostrar características adicionales
        print("\n=== CARACTERÍSTICAS ADICIONALES ===")
        for feature, details in self.additional_features.items():
            if details["available"]:
                premium_tag = " (Premium)" if details["premium"] else ""
                print(f"- {feature}: ${details['price']}{premium_tag}")
        
        # Seleccionar características adicionales
        selected_features = []
        while True:
            feature = input("\nAgregar característica (o 'fin' para terminar): ")
            if feature.lower() == 'fin':
                break
            
            if feature in self.additional_features and self.additional_features[feature]["available"]:
                selected_features.append(feature)
                print(f"Agregado: {feature}")
            else:
                print("Característica no válida o no disponible. Intente nuevamente.")
        
        # Calcular y mostrar resumen
        result = self.calculate_total_cost(selected_plan, selected_features)
        
        if result == -1:
            return -1
        
        final_cost, base_cost, features_cost, discount, premium_surcharge = result
        
        # Mostrar resumen para confirmación
        print("\n=== RESUMEN DE MEMBRESÍA ===")
        print(f"Plan seleccionado: {selected_plan} (${base_cost})")
        print("Características adicionales:")
        for feature in selected_features:
            print(f"- {feature}: ${self.additional_features[feature]['price']}")
        
        print(f"\nSubtotal: ${base_cost + features_cost}")
        
        if discount > 0:
            print(f"Descuento aplicado: -${discount}")
            
        if premium_surcharge > 0:
            print(f"Recargo por características premium (15%): +${premium_surcharge}")
        
        print(f"TOTAL: ${final_cost}")
        
        # Confirmación del usuario
        confirmation = input("\n¿Confirmar membresía? (s/n): ")
        if confirmation.lower() == 's':
            print("¡Membresía confirmada!")
            return final_cost
        else:
            print("Membresía cancelada.")
            return -1

# Función principal
def main():
    print("=== SISTEMA DE MEMBRESÍAS DE GIMNASIO ===")
    gym_system = GymMembershipSystem()
    result = gym_system.process_membership()
    
    if result > 0:
        print(f"\nCosto total de la membresía: ${result}")
    else:
        print("\nOperación no completada.")

if __name__ == "__main__":
    main()
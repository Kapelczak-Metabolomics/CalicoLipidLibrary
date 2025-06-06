from lipidRules import *


class Alkyl_PS(alkylGPL):
    def theoreticalDigest(self):
        FRAGMENTS = []
        adduct = self.adduct

        MASS = MW_list(self.MF())
        PREC = MASS + ADDUCT[self.adduct]
        FRAGMENTS.append([PREC, 1000, "precursor"])

        if adduct in POS_ADDUCTS:
            FRAGMENTS.append([PREC - H2O, 1000, "NL water"])  # C3H8NO6P

        #
        # 				if adduct == "[M+H]+":
        # 					FRAGMENTS.append( [PREC-H2O, 1000, "NL water"] ) #C3H8NO6P
        # 					FRAGMENTS.append( [PREC-MW("C3H8NO6P"), 1000, "NL phosphoserine"] ) #C3H8NO6P
        # 					FRAGMENTS.append( [MW("C3H7NO3")+ADDUCT[adduct], 1000,  "Serine"] ) #Ser
        # 					FRAGMENTS.append( [MW("C3H7NO3")+ADDUCT[adduct]-H2O, 1000,  "Serine - water"] ) #Ser
        # 					FRAGMENTS.append( [MW("C3H9O6P")+ADDUCT[adduct]-H2O, 1000,  "Glycerol-P - water"] )
        #
        #
        # 					for i in range(0,len(self.chains)):
        # 						chain = str(i+1)
        # 						FRAGMENTS.append( [PREC - NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i])+H2O, 1000, "sn" + chain])
        # 						FRAGMENTS.append( [PREC - NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i]), 1000, "sn" + chain +"-H2O"])
        # 						FRAGMENTS.append( [NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i])-H2O+ADDUCT[adduct], 1000, "sn" + chain +" acylium ion"])
        # 						FRAGMENTS.append( [NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i])-H2O-H2O+ADDUCT[adduct], 1000, "sn" + chain +" acylium ion - H2O"])
        # 						FRAGMENTS.append( [NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i])-H2O+MW("C3H6O2")+ADDUCT[adduct], 1000, "sn" + chain +" + C3H6O2 (from glycerol)"])
        # 						FRAGMENTS.append( [NL(self.chains[i], self.doublebonds[i],self.hydroxyls[i])-H2O+MW("C3H5NO2")+ADDUCT[adduct], 1000, "sn" + chain +" + C3H5NO2"])
        #
        #
        #
        #
        # 				if adduct == "[M+Na]+" or adduct == "[M+NH4]+" or adduct == "[M+K]+":
        # 					FRAGMENTS.append( [PREC-MW("C3H8NO6P")+PROTON-ADDUCT[adduct], 1000,  "precursor - P-Ser - adduct"] )
        # 					FRAGMENTS.append( [MW("C3H8NO6P")+ADDUCT[adduct], 1000,  " P-Ser+adduct"] )
        # 					FRAGMENTS.append( [MW("C3H8NO6P")+ADDUCT[adduct], 1000,  " headgroup+adduct-Ser"] )
        # 					FRAGMENTS.append( [MW("H3PO4")+ADDUCT[adduct], 1000,  " H3PO4+adduct"] )
        #
        #

        elif adduct in NEG_ADDUCTS:
            FRAGMENTS.append([MW("H3PO4") - PROTON, 1000, "phosphate"])
            FRAGMENTS.append([MW("HPO3") - PROTON, 1000, "phosphite"])
            FRAGMENTS.append([PREC - MW("C3H5NO2"), 1000, "NL Serine"])

            FRAGMENTS.append([MW("C3H7O5P") - PROTON, 1000, "C3H6O5P-"])
            FRAGMENTS.append([MW("C3H9O6P") - PROTON, 1000, "C3H8O6P-"])

            for i in [1]:
                chain = str(i + 1)
                FRAGMENTS.append(
                    [NL(self.chains[i]) - PROTON, 1000, "sn" + chain + " RCO2-"]
                )
                FRAGMENTS.append(
                    [
                        PREC - MW("C3H5NO2") - NL(self.chains[i]) + H2O,
                        1000,
                        "NL (Serine + sn" + chain + "ketene)",
                    ]
                )
                FRAGMENTS.append(
                    [
                        PREC - MW("C3H5NO2") - NL(self.chains[i]),
                        1000,
                        "NL Serine + sn" + chain + ")",
                    ]
                )

        return FRAGMENTS


# x  = Alkyl_PS("Alkyl_PS",[[16,0,0], [18,2,0]],  adduct="[M+H]+")
# print x.printNist()

# calicolipidlibrary.print_spectrum("Alkyl_PS", [[16,0,0], [18,2,0]], "[M+H]+")

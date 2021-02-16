import requests

result_str = """{
  "data": {
    "carAll": {
      "edges": [
        {
          "node": {
            "id": "Q2FyTm9kZToxMTU3",
            "constructioninterval": "08.1976 - 07.1982",
            "description": "1.6",
            "fulldescription": "AUDI 100 (43, C2) 1.6",
            "engines": {
              "edges": [
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozNjI=",
                    "description": "YV",
                    "fulldescription": "AUDI YV",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "63 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "85 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "1588 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "8.2 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "80 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "4"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "8"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "Q2FyTm9kZToxMTYw",
            "constructioninterval": "08.1980 - 07.1982",
            "description": "1.9",
            "fulldescription": "AUDI 100 (43, C2) 1.9",
            "engines": {
              "edges": [
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzY=",
                    "description": "WH",
                    "fulldescription": "AUDI WH",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": "02.1983 - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "74 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "100 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "1921 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "Super (98) этилированный"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "10 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "77.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "Q2FyTm9kZToxMjk3",
            "constructioninterval": "06.1976 - 08.1978",
            "description": "2.0",
            "fulldescription": "AUDI 100 (43, C2) 2.0",
            "engines": {
              "edges": [
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMjk=",
                    "description": "WA",
                    "fulldescription": "AUDI WA",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "85 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "115 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "1984 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "9.3 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "86.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "84.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "4"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "8"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "Q2FyTm9kZToxMjk4",
            "constructioninterval": "10.1977 - 07.1982",
            "description": "2.1",
            "fulldescription": "AUDI 100 (43, C2) 2.1",
            "engines": {
              "edges": [
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzA=",
                    "description": "WB",
                    "fulldescription": "AUDI WB",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "85 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "115 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "9.3 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                },
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzM=",
                    "description": "WE",
                    "fulldescription": "AUDI WE",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "75 - 85 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "102 - 115 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "8.2 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                },
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzM=",
                    "description": "WE",
                    "fulldescription": "AUDI WE",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "75 - 85 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "102 - 115 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "8.2 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "Q2FyTm9kZToxMjk5",
            "constructioninterval": "03.1977 - 07.1982",
            "description": "2.1",
            "fulldescription": "AUDI 100 (43, C2) 2.1",
            "engines": {
              "edges": [
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzE=",
                    "description": "WC",
                    "fulldescription": "AUDI WC",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": "10.1979 - 07.1984"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "100 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "136 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "Супер-бензин (95) неэтилированный"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Compression",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Compression",
                            "displayvalue": "9.3 : 1"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                },
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzU=",
                    "description": "WG",
                    "fulldescription": "AUDI WG",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "100 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "136 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                },
                {
                  "node": {
                    "id": "RW5naW5lTm9kZTozMzU=",
                    "description": "WG",
                    "fulldescription": "AUDI WG",
                    "engineattributeSet": {
                      "edges": [
                        {
                          "node": {
                            "attributetype": "ConstructionInterval",
                            "attributegroup": "General",
                            "displaytitle": "Construction interval",
                            "displayvalue": " - "
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "100 kW"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Power",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Power",
                            "displayvalue": "136 PS"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Capacity",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Capacity",
                            "displayvalue": "2144 ccm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine construction",
                            "displayvalue": "ряд"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel type",
                            "displayvalue": "бензин"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "FuelMixture",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Fuel mixture",
                            "displayvalue": "Впрыскивание во впускной коллектор/Карбюратор"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineType",
                            "attributegroup": "General",
                            "displaytitle": "Engine type",
                            "displayvalue": "Бензиновый двигатель"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CylinderConstruction",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cylinder construction",
                            "displayvalue": "SOHC/OHC"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "EngineManagement",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Engine management",
                            "displayvalue": "Зубчатый ремень"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "CoolingType",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Cooling type",
                            "displayvalue": "с водяным охлаждением"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Bore",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Bore",
                            "displayvalue": "79.5 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "Stroke",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Stroke",
                            "displayvalue": "86.4 mm"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfCylinders",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of cylinders",
                            "displayvalue": "5"
                          }
                        },
                        {
                          "node": {
                            "attributetype": "NumberOfValves",
                            "attributegroup": "TechnicalData",
                            "displaytitle": "Number of valves",
                            "displayvalue": "10"
                          }
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}"""

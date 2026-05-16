#!/usr/bin/env python3
"""
Script para generar imágenes PNG desde archivos PlantUML
Utiliza el servicio en línea de PlantUML
"""

import urllib.request
import urllib.error
import base64
import zlib
import os
from pathlib import Path

def encode_plantuml(puml_text):
    """Codifica texto PlantUML para usar en URL"""
    # Comprimir con zlib
    compressed = zlib.compress(puml_text.encode('utf-8'), 9)
    # Codificar en base64
    encoded = base64.b64encode(compressed).decode('ascii')
    return encoded

def generate_png_from_url(encoded, output_file):
    """Genera PNG usando servicio web de PlantUML"""
    url = f'https://www.plantuml.com/plantuml/png/{encoded}'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=60) as response:
            if response.status == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.read())
                return True, "OK"
            else:
                return False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP Error {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return False, f"URL Error: {e.reason}"
    except Exception as e:
        return False, f"Exception: {str(e)}"

def main():
    """Genera PNGs para todos los diagramas"""
    
    diagrams = [
        ('diagramas/05-diagramas-secuencia/05-secuencia-agendar-turno-flujo-principal-01.puml',
         'diagramas/05-diagramas-secuencia/05-secuencia-agendar-turno-flujo-principal-01.png'),
        ('diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.puml',
         'diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.png'),
        ('diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.puml',
         'diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.png'),
        ('diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-flujo-principal-04.puml',
         'diagramas/05-diagramas-secuencia/05-secuencia-autorizar-sobreturno-flujo-principal-04.png'),
        ('diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.puml',
         'diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.png'),
    ]
    
    print("=" * 70)
    print("Generador de PNG desde PlantUML")
    print("=" * 70)
    
    generated = 0
    failed = 0
    
    for puml_file, png_file in diagrams:
        if not os.path.exists(puml_file):
            print(f"✗ {png_file:<60} - Archivo PUML no encontrado")
            failed += 1
            continue
        
        try:
            with open(puml_file, 'r', encoding='utf-8') as f:
                puml_content = f.read()
            
            print(f"  Codificando: {Path(puml_file).name:<50}", end=" ")
            encoded = encode_plantuml(puml_content)
            print("OK")
            
            print(f"  Generando : {Path(png_file).name:<50}", end=" ")
            success, message = generate_png_from_url(encoded, png_file)
            
            if success:
                print(f"✓ {message}")
                generated += 1
            else:
                print(f"✗ {message}")
                failed += 1
        
        except Exception as e:
            print(f"✗ {png_file:<60} - {str(e)}")
            failed += 1
    
    print("=" * 70)
    print(f"Resultados: {generated} generados, {failed} fallidos")
    print("=" * 70)
    
    return 0 if failed == 0 else 1

if __name__ == '__main__':
    exit(main())

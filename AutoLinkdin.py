from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def busca_linkedin():
    navegador = webdriver.Chrome()
    try:
        navegador.get("https://www.google.com")

        campo_busca = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        campo_busca.send_keys("LinkedIn")

        botao = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK')))
        botao.click()

        navegador.find_element(By.CLASS_NAME, 'LC20lb').click()

        navegador.get("https://www.linkedin.com/login/")
        navegador.find_element(By.ID, "username").send_keys("marcosfelipe@reborntechnology.tech")
        navegador.find_element(By.ID, "password").send_keys("reborn2024")

        botao = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        botao.click()

        WebDriverWait(navegador, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Pesquisar"]')))

        campo_busca_linkedin = navegador.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
        campo_busca_linkedin.send_keys('Recepcionista' + Keys.ENTER)

        botao = WebDriverWait(navegador, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".artdeco-pill.search-reusables__filter-pill-button")))
        botao.click()

        elementos_nome_vaga = WebDriverWait(navegador, 30).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container__link.job-card-list__title.job-card-list__title--link")))

        elemento_localizacao = WebDriverWait(navegador, 30).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'job-card-container__metadata-item')))

        print("Resultados LinkedIn:")
        for vaga, localizacao in zip(elementos_nome_vaga, elemento_localizacao):
            print(f"Vaga: {vaga.text}")
            print(f"Localização: {localizacao.text}\n")

    finally:
        navegador.quit()


def busca_gupy():
    navegador = webdriver.Chrome()
    try:
        navegador.get("https://www.google.com")

        campo_busca = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        campo_busca.send_keys("Gupy")

        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

        navegador.find_element(By.CLASS_NAME, 'LC20lb').click()

        navegador.get("https://login.gupy.io/candidates/signin")

        try:
            consent_banner = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cc-btn.cc-deny')))
            consent_banner.click()
        except Exception:
            print("Banner de consentimento não encontrado ou já foi fechado.")

        username_input = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.ID, "username")))
        username_input.send_keys("joaquimcarlostimoteo1@gmail.com")
        navegador.find_element(By.NAME, "password").send_keys("m$qbmS*?edm8!#$")
        navegador.find_element(By.ID, 'button-signin').click()

        try:
            fechar_banner = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.ID, "pushActionRefuse")))
            fechar_banner.click()
        except Exception:
            print("Banner de consentimento não encontrado ou já foi fechado.")

        avatar_elemento = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'avatar') and contains(@class, 'avatar__default')]")))
        avatar_elemento.click()

        avatar_elemento = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='access-portal-button']")))
        avatar_elemento.click()

        campo_busca = WebDriverWait(navegador, 30).until(EC.element_to_be_clickable((By.NAME, 'searchTerm')))
        campo_busca.send_keys("Desenvolvedor Front-end")

        WebDriverWait(navegador, 30).until(EC.element_to_be_clickable((By.ID, 'undefined-button'))).click()

        elementos_nome_vaga = WebDriverWait(navegador, 30).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, 'h3')))

        elemento_localizacao = WebDriverWait(navegador, 30).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="job-location"]')))

        print("Resultados Gupy:")
        for vaga, localizacao in zip(elementos_nome_vaga, elemento_localizacao):
            print(f"Vaga: {vaga.text}")
            print(f"Localização: {localizacao.text}\n")

    finally:
        navegador.quit()

if __name__ == "__main__":
    busca_gupy()
    busca_linkedin()

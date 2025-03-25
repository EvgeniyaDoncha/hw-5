import command
from selene.support.shared import browser
from selene import have
import os



def test_student_registration_form():
    browser.open('/automation-practice-form')


    # WHEN
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('YA')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    '''
    browser.all('[name=gender]').element_by(have.value('Female')).element(
        './following-sabling::*'
    ).click()
    browser.element('[name=gender] [value=Female]+label').click()
    browser.element('[value=Female+label]').click()
    '''
    browser.element('#userNumber').type('1234567891')
    browser.element('#userEmail').type('name@example.com')

    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()

    browser.element('#currentAddress').type('Moscowskaya Street 18')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_texts('HCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_texts('Noida')
    ).click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element(f'.react-datepicker__day--0{11}').click()


    browser.element('#subjectsInput').type('Commerce').press_enter()

    import tests
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )


    browser.element('#submit').press_enter()
    browser.element('#submit').perform(command.js.click)

    #THEN
    browser.all('.table-responsive td:nth-child(2)').should(
        have.texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi'
        )
    )

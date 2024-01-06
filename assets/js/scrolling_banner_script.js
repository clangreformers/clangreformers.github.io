// script.js

const glossaries = document.querySelectorAll('.glossary');

glossaries.forEach((glossary) => {
    glossary.addEventListener('click', () => {
        const text = glossary.textContent;
        // Replace with the URLs you want to navigate to based on the clicked word
        switch (text) {
            case 'Mandarin Language Movement...':
                window.location.href = '/glossary/movement';
                break;
            case 'Pronunciation Standardization Association...':
                window.location.href = '/glossary/pronunciation';
                break;
            case 'Mandarin Language Research Association...':
                window.location.href = '/glossary/research';
                break;
            case 'National Language Unification Preparation Committee...':
                window.location.href = '/glossary/preparation';
                break;
            case 'Several Persons Club♦♦♦':
                window.location.href = '/glossary/persons';
                break;
            case 'Compilation Department of the Chinese Great Dictionary...':
                window.location.href = '/glossary/compilation';
                break;
            case 'Phonetic symbols...':
                window.location.href = 'https://en.wikipedia.org/wiki/Bopomofo';
                break;
            case 'Mandarin Romanization...':
                window.location.href = 'https://en.wikipedia.org/wiki/Gwoyeu_Romatzyh';
                break;
            // Simplified Chinese
            case '国语运动...':
                window.location.href = '/glossary/movement-cn';
                break;
            case '读音统一会...':
                window.location.href = '/glossary/pronunciation-cn';
                break;
            case '国语研究会...':
                window.location.href = '/glossary/research-cn';
                break;
            case '国语统一筹备会...':
                window.location.href = '/glossary/preparation-cn';
                break;
            case '数人会...':
                window.location.href = '/glossary/persons-cn';
                break;
            case '中国大辞典编纂处...':
                window.location.href = '/glossary/compilation-cn';
                break;
            case '注音符号...':
                window.location.href = 'https://baike.baidu.com/item/%E6%B1%89%E8%AF%AD%E6%B3%A8%E9%9F%B3%E7%AC%A6%E5%8F%B7/115195';
                break;
            case '国语罗马字...':
                window.location.href = 'https://baike.baidu.com/item/%E5%9B%BD%E8%AF%AD%E7%BD%97%E9%A9%AC%E5%AD%97/6060641';
                break;
			// Traditional Chinese
            case '國語運動...':
                window.location.href = '/glossary/movement-tw';
                break;
            case '讀音統一會...':
                window.location.href = '/glossary/pronunciation-tw';
                break;
            case '國語研究會...':
                window.location.href = '/glossary/research-tw';
                break;
            case '國語統一籌備會...':
                window.location.href = '/glossary/preparation-tw';
                break;
            case '數人會...':
                window.location.href = '/glossary/persons-tw';
                break;
            case '中國大辭典編纂處...':
                window.location.href = '/glossary/compilation-tw';
                break;
            case '注音符號...':
                window.location.href = 'https://zh.wikipedia.org/zh-hans/%E6%B3%A8%E9%9F%B3%E7%AC%A6%E8%99%9F';
                break;
            case '國語羅馬字...':
                window.location.href = 'https://zh.wikipedia.org/zh-tw/%E5%9C%8B%E8%AA%9E%E7%BE%85%E9%A6%AC%E5%AD%97';
                break;				
        }
    });
});
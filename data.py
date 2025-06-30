class Data:

    BROWSER_NAME = None
    EMAIL = "timofei_vasilev_20_123@yandex.ru"
    PASSWORD = "1qazXSW@"
    SCRIPT ="""
                const [from_element, to_element] = arguments;
                const dataTransfer = new DataTransfer();
                ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                    const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                    (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                });
            """
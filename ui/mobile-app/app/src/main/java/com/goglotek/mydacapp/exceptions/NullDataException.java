package com.goglotek.mydacapp.exceptions;

public class NullDataException extends GoglotekException {
    public NullDataException() {
        super();
    }

    public NullDataException(String msg) {
        super(msg);
    }

    public NullDataException(String msg, Throwable cause) {
        super(msg, cause);
    }

}


package com.goglotek.mydacapp.exceptions;

public class GoglotekException extends Exception {
    public GoglotekException() {
        super();
    }

    public GoglotekException(String msg) {
        super(msg);
    }

    public GoglotekException(String msg, Throwable cause) {
        super(msg, cause);
    }

}

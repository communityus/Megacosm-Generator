#!/usr/bin/env python
import megacosm

megacosm.app.config.from_object('config.DevConfiguration')


megacosm.app.run(host='0.0.0.0', port=8000, debug=True)

// -*- lsst-c++ -*-
/*
 * LSST Data Management System
 * Copyright 2008-2013 LSST Corporation.
 *
 * This product includes software developed by the
 * LSST Project (http://www.lsst.org/).
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the LSST License Statement and
 * the GNU General Public License along with this program.  If not,
 * see <http://www.lsstcorp.org/LegalNotices/>.
 */

#ifndef LSST_MEAS_MODELFIT_Sampler_h_INCLUDED
#define LSST_MEAS_MODELFIT_Sampler_h_INCLUDED

#include "lsst/afw/table/fwd.h"
#include "lsst/meas/modelfit/Mixture.h"
#include "lsst/meas/modelfit/Sampling.h"

namespace lsst { namespace meas { namespace modelfit {

class Sampler {
public:

    virtual void run(
        SamplingObjective const & objective,
        PTR(Mixture) proposal,
        afw::table::BaseCatalog & samples
    ) const = 0;

    virtual ~Sampler() {}

};

}}} // namespace lsst::meas::modelfit

#endif // !LSST_MEAS_MODELFIT_Sampler_h_INCLUDED
